from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime
import os
from config import config

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    return app

app = create_app()
db = SQLAlchemy(app)

# Modelos do banco de dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    fonte_conhecimento = db.Column(db.String(100), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    respostas = db.relationship('Resposta', backref='usuario', lazy=True)

class Questao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pergunta = db.Column(db.Text, nullable=False)
    opcao_a = db.Column(db.String(200), nullable=False)
    opcao_b = db.Column(db.String(200), nullable=False)
    opcao_c = db.Column(db.String(200), nullable=False)
    opcao_d = db.Column(db.String(200), nullable=False)
    resposta_correta = db.Column(db.String(1), nullable=False)  # A, B, C ou D

class Resposta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    questao_id = db.Column(db.Integer, db.ForeignKey('questao.id'), nullable=False)
    resposta_escolhida = db.Column(db.String(1), nullable=False)
    esta_correta = db.Column(db.Boolean, nullable=False)
    data_resposta = db.Column(db.DateTime, default=datetime.utcnow)

class Resultado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    total_acertos = db.Column(db.Integer, nullable=False)
    total_questoes = db.Column(db.Integer, nullable=False)
    ganhou_brinde = db.Column(db.Boolean, nullable=False)
    data_resultado = db.Column(db.DateTime, default=datetime.utcnow)

# Rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/quiz')
def quiz():
    if 'usuario_id' not in session:
        return redirect(url_for('formulario'))
    return render_template('quiz.html')

@app.route('/resultado')
def resultado():
    if 'usuario_id' not in session:
        return redirect(url_for('formulario'))
    return render_template('resultado.html')

# APIs
@app.route('/api/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    print("=== API CADASTRAR USUARIO CHAMADA ===")
    try:
        data = request.get_json()
        print(f"Dados recebidos: {data}")
        
        # Validar dados obrigatórios
        if not all(key in data for key in ['nome', 'idade', 'genero', 'fonte_conhecimento']):
            print("Erro: Dados obrigatórios faltando")
            return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400
        
        # Criar usuário
        usuario = Usuario(
            nome=data['nome'],
            idade=data['idade'],
            genero=data['genero'],
            fonte_conhecimento=data['fonte_conhecimento']
        )
        
        print(f"Usuário criado: {usuario.nome}")
        
        db.session.add(usuario)
        db.session.commit()
        
        print(f"Usuário salvo no banco com ID: {usuario.id}")
        
        # Salvar ID na sessão
        session['usuario_id'] = usuario.id
        
        print("ID salvo na sessão")
        
        response_data = {'sucesso': True, 'usuario_id': usuario.id}
        print(f"Retornando: {response_data}")
        return jsonify(response_data)
    
    except Exception as e:
        print(f"Erro na API: {str(e)}")
        db.session.rollback()
        return jsonify({'erro': str(e)}), 500

@app.route('/api/obter_questoes', methods=['GET'])
def obter_questoes():
    if 'usuario_id' not in session:
        return jsonify({'erro': 'Usuário não autenticado'}), 401
    
    try:
        # Buscar todas as questões
        todas_questoes = Questao.query.all()
        
        if len(todas_questoes) < 7:
            return jsonify({'erro': 'Não há questões suficientes no banco'}), 400
        
        # Sortear 7 questões
        questoes_sorteadas = random.sample(todas_questoes, 7)
        
        questoes_data = []
        for questao in questoes_sorteadas:
            questoes_data.append({
                'id': questao.id,
                'pergunta': questao.pergunta,
                'opcoes': {
                    'A': questao.opcao_a,
                    'B': questao.opcao_b,
                    'C': questao.opcao_c,
                    'D': questao.opcao_d
                }
            })
        
        # Salvar questões sorteadas na sessão
        session['questoes_quiz'] = [q.id for q in questoes_sorteadas]
        
        return jsonify({'questoes': questoes_data})
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/enviar_respostas', methods=['POST'])
def enviar_respostas():
    print("=== API ENVIAR RESPOSTAS CHAMADA ===")
    if 'usuario_id' not in session:
        print("Erro: Usuário não autenticado")
        return jsonify({'erro': 'Usuário não autenticado'}), 401
    
    if 'questoes_quiz' not in session:
        print("Erro: Quiz não iniciado")
        return jsonify({'erro': 'Quiz não iniciado'}), 400
    
    try:
        data = request.get_json()
        respostas = data.get('respostas', [])
        usuario_id = session['usuario_id']
        
        print(f"Usuario ID: {usuario_id}")
        print(f"Respostas recebidas: {respostas}")
        print(f"Número de respostas: {len(respostas)}")
        
        if len(respostas) != 7:
            print(f"Erro: Número incorreto de respostas. Esperado: 7, Recebido: {len(respostas)}")
            return jsonify({'erro': 'Número incorreto de respostas'}), 400
        
        acertos = 0
        respostas_salvas = []
        
        # Processar cada resposta
        for i, resposta_data in enumerate(respostas):
            questao_id = resposta_data['questao_id']
            resposta_escolhida = resposta_data['resposta']
            
            print(f"Processando resposta {i+1}: Questão {questao_id}, Resposta: {resposta_escolhida}")
            
            # Buscar questão
            questao = Questao.query.get(questao_id)
            if not questao:
                print(f"Erro: Questão {questao_id} não encontrada")
                continue
            
            # Verificar se está correta
            esta_correta = resposta_escolhida == questao.resposta_correta
            if esta_correta:
                acertos += 1
                print(f"✓ Resposta correta para questão {questao_id}")
            else:
                print(f"✗ Resposta incorreta para questão {questao_id}. Esperado: {questao.resposta_correta}, Recebido: {resposta_escolhida}")
            
            # Salvar resposta
            resposta = Resposta(
                usuario_id=usuario_id,
                questao_id=questao_id,
                resposta_escolhida=resposta_escolhida,
                esta_correta=esta_correta
            )
            db.session.add(resposta)
            respostas_salvas.append(resposta)
            
            print(f"Resposta salva no banco: ID={resposta.id}, Usuario={usuario_id}, Questao={questao_id}, Escolhida={resposta_escolhida}, Correta={esta_correta}")
        
        print(f"Total de acertos: {acertos}/7")
        
        # Determinar se ganhou brinde (mais da metade)
        ganhou_brinde = acertos > 3  # Mais de 3 acertos em 7 questões
        print(f"Ganhou brinde: {ganhou_brinde}")
        
        # Salvar resultado
        resultado = Resultado(
            usuario_id=usuario_id,
            total_acertos=acertos,
            total_questoes=7,
            ganhou_brinde=ganhou_brinde
        )
        db.session.add(resultado)
        
        # Commit das mudanças
        db.session.commit()
        
        print(f"Resultado salvo no banco: ID={resultado.id}, Usuario={usuario_id}, Acertos={acertos}, Ganhou={ganhou_brinde}")
        print(f"Total de respostas salvas: {len(respostas_salvas)}")
        
        # Limpar dados da sessão
        session.pop('questoes_quiz', None)
        print("Dados do quiz removidos da sessão")
        
        response_data = {
            'acertos': acertos,
            'total': 7,
            'ganhou_brinde': ganhou_brinde,
            'respostas_salvas': len(respostas_salvas)
        }
        
        print(f"Retornando: {response_data}")
        return jsonify(response_data)
    
    except Exception as e:
        print(f"Erro na API: {str(e)}")
        print(f"Traceback: {e.__traceback__}")
        db.session.rollback()
        return jsonify({'erro': str(e)}), 500

@app.route('/api/obter_resultado', methods=['GET'])
def obter_resultado():
    if 'usuario_id' not in session:
        return jsonify({'erro': 'Usuário não autenticado'}), 401
    
    try:
        usuario_id = session['usuario_id']
        resultado = Resultado.query.filter_by(usuario_id=usuario_id).order_by(Resultado.data_resultado.desc()).first()
        
        if not resultado:
            return jsonify({'erro': 'Resultado não encontrado'}), 404
        
        return jsonify({
            'acertos': resultado.total_acertos,
            'total': resultado.total_questoes,
            'ganhou_brinde': resultado.ganhou_brinde
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/consultar_respostas', methods=['GET'])
def consultar_respostas():
    """API para consultar todas as respostas de um usuário (para debug)"""
    if 'usuario_id' not in session:
        return jsonify({'erro': 'Usuário não autenticado'}), 401
    
    try:
        usuario_id = session['usuario_id']
        
        # Buscar todas as respostas do usuário
        respostas = Resposta.query.filter_by(usuario_id=usuario_id).all()
        
        # Buscar o resultado do usuário
        resultado = Resultado.query.filter_by(usuario_id=usuario_id).order_by(Resultado.data_resultado.desc()).first()
        
        # Buscar dados do usuário
        usuario = Usuario.query.get(usuario_id)
        
        respostas_data = []
        for resposta in respostas:
            questao = Questao.query.get(resposta.questao_id)
            respostas_data.append({
                'id': resposta.id,
                'questao_id': resposta.questao_id,
                'pergunta': questao.pergunta if questao else 'Questão não encontrada',
                'resposta_escolhida': resposta.resposta_escolhida,
                'resposta_correta': questao.resposta_correta if questao else 'N/A',
                'esta_correta': resposta.esta_correta,
                'data_resposta': resposta.data_resposta.isoformat() if resposta.data_resposta else None
            })
        
        return jsonify({
            'usuario': {
                'id': usuario.id,
                'nome': usuario.nome,
                'idade': usuario.idade,
                'genero': usuario.genero,
                'fonte_conhecimento': usuario.fonte_conhecimento,
                'data_cadastro': usuario.data_cadastro.isoformat() if usuario.data_cadastro else None
            },
            'resultado': {
                'id': resultado.id,
                'total_acertos': resultado.total_acertos,
                'total_questoes': resultado.total_questoes,
                'ganhou_brinde': resultado.ganhou_brinde,
                'data_resultado': resultado.data_resultado.isoformat() if resultado.data_resultado else None
            } if resultado else None,
            'respostas': respostas_data,
            'total_respostas': len(respostas_data)
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/limpar_sessao', methods=['POST'])
def limpar_sessao():
    session.clear()
    return jsonify({'sucesso': True})

@app.route('/admin/dados', methods=['GET'])
def visualizar_dados():
    """Rota para visualizar todos os dados do banco (para debug)"""
    try:
        # Buscar todos os usuários
        usuarios = Usuario.query.all()
        usuarios_data = []
        
        for usuario in usuarios:
            # Buscar respostas do usuário
            respostas = Resposta.query.filter_by(usuario_id=usuario.id).all()
            respostas_data = []
            
            for resposta in respostas:
                questao = Questao.query.get(resposta.questao_id)
                respostas_data.append({
                    'questao_id': resposta.questao_id,
                    'pergunta': questao.pergunta if questao else 'N/A',
                    'resposta_escolhida': resposta.resposta_escolhida,
                    'resposta_correta': questao.resposta_correta if questao else 'N/A',
                    'esta_correta': resposta.esta_correta,
                    'data_resposta': resposta.data_resposta.isoformat() if resposta.data_resposta else None
                })
            
            # Buscar resultado do usuário
            resultado = Resultado.query.filter_by(usuario_id=usuario.id).order_by(Resultado.data_resultado.desc()).first()
            
            usuarios_data.append({
                'id': usuario.id,
                'nome': usuario.nome,
                'idade': usuario.idade,
                'genero': usuario.genero,
                'fonte_conhecimento': usuario.fonte_conhecimento,
                'data_cadastro': usuario.data_cadastro.isoformat() if usuario.data_cadastro else None,
                'respostas': respostas_data,
                'total_respostas': len(respostas_data),
                'resultado': {
                    'total_acertos': resultado.total_acertos,
                    'total_questoes': resultado.total_questoes,
                    'ganhou_brinde': resultado.ganhou_brinde,
                    'data_resultado': resultado.data_resultado.isoformat() if resultado.data_resultado else None
                } if resultado else None
            })
        
        # Estatísticas gerais
        total_usuarios = len(usuarios)
        total_respostas = Resposta.query.count()
        total_resultados = Resultado.query.count()
        ganharam_brinde = Resultado.query.filter_by(ganhou_brinde=True).count()
        
        return jsonify({
            'estatisticas': {
                'total_usuarios': total_usuarios,
                'total_respostas': total_respostas,
                'total_resultados': total_resultados,
                'ganharam_brinde': ganharam_brinde,
                'nao_ganharam_brinde': total_resultados - ganharam_brinde
            },
            'usuarios': usuarios_data
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Inserir questões de exemplo se não existirem
        if Questao.query.count() == 0:
            questoes_exemplo = [
                {
                    'pergunta': 'Qual é o principal benefício do uso de protetor solar?',
                    'opcao_a': 'Bronzear mais rápido',
                    'opcao_b': 'Proteger contra câncer de pele',
                    'opcao_c': 'Hidratar a pele',
                    'opcao_d': 'Remover manchas',
                    'resposta_correta': 'B'
                },
                {
                    'pergunta': 'Quantas vezes por dia é recomendado lavar o rosto?',
                    'opcao_a': '1 vez',
                    'opcao_b': '2 vezes',
                    'opcao_c': '4 vezes',
                    'opcao_d': '6 vezes',
                    'resposta_correta': 'B'
                },
                {
                    'pergunta': 'Qual vitamina é essencial para a saúde da pele?',
                    'opcao_a': 'Vitamina A',
                    'opcao_b': 'Vitamina B',
                    'opcao_c': 'Vitamina C',
                    'opcao_d': 'Todas as anteriores',
                    'resposta_correta': 'D'
                },
                {
                    'pergunta': 'O que causa o envelhecimento precoce da pele?',
                    'opcao_a': 'Exposição ao sol',
                    'opcao_b': 'Poluição',
                    'opcao_c': 'Tabagismo',
                    'opcao_d': 'Todas as anteriores',
                    'resposta_correta': 'D'
                },
                {
                    'pergunta': 'Qual é a função do ácido hialurônico na pele?',
                    'opcao_a': 'Esfoliar',
                    'opcao_b': 'Hidratar e reter água',
                    'opcao_c': 'Clarear manchas',
                    'opcao_d': 'Contrair poros',
                    'resposta_correta': 'B'
                },
                {
                    'pergunta': 'Qual o melhor horário para aplicar protetor solar?',
                    'opcao_a': 'À noite',
                    'opcao_b': '30 minutos antes da exposição',
                    'opcao_c': 'Durante a exposição',
                    'opcao_d': 'Depois da exposição',
                    'resposta_correta': 'B'
                },
                {
                    'pergunta': 'O que significa FPS no protetor solar?',
                    'opcao_a': 'Fator de Proteção Solar',
                    'opcao_b': 'Filtro de Proteção Solar',
                    'opcao_c': 'Fórmula de Proteção Solar',
                    'opcao_d': 'Fator de Proteção da Pele',
                    'resposta_correta': 'A'
                },
                {
                    'pergunta': 'Qual ingrediente é conhecido por combater rugas?',
                    'opcao_a': 'Retinol',
                    'opcao_b': 'Glicerina',
                    'opcao_c': 'Óleo de coco',
                    'opcao_d': 'Água termal',
                    'resposta_correta': 'A'
                },
                {
                    'pergunta': 'Quantos litros de água devemos beber por dia?',
                    'opcao_a': '1 litro',
                    'opcao_b': '2 litros',
                    'opcao_c': '3 litros',
                    'opcao_d': '4 litros',
                    'resposta_correta': 'B'
                },
                {
                    'pergunta': 'Qual é a função da vitamina C na pele?',
                    'opcao_a': 'Hidratar',
                    'opcao_b': 'Antioxidante e clarear',
                    'opcao_c': 'Esfoliar',
                    'opcao_d': 'Contrair poros',
                    'resposta_correta': 'B'
                }
            ]
            
            for q in questoes_exemplo:
                questao = Questao(**q)
                db.session.add(questao)
            
            db.session.commit()
    
    app.run(debug=True)
