# Quiz Beleza que Respira

Uma aplicação Flask completa para um quiz interativo sobre cuidados com a pele, com sistema de cadastro, questões sorteadas e prêmios.

## 🚀 Funcionalidades

- **Tela de Boas-vindas**: Apresentação do quiz com instruções
- **Formulário de Cadastro**: Coleta dados obrigatórios do usuário
- **Quiz Dinâmico**: 7 questões sorteadas de um banco de ~50 questões
- **Sistema de Correção**: Avaliação automática das respostas
- **Resultados**: Exibição de pontuação e prêmios
- **Banco de Dados**: Armazenamento de usuários, respostas e resultados

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🛠️ Instalação

1. **Clone o repositório**:
```bash
git clone <url-do-repositorio>
cd quiz-beleza-que-respira
```

2. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**:
```bash
python app.py
```

4. **Acesse no navegador**:
```
http://localhost:5000
```

## 🗄️ Estrutura do Banco de Dados

### Tabelas

- **Usuario**: Dados pessoais dos participantes
- **Questao**: Banco de questões do quiz
- **Resposta**: Respostas individuais de cada usuário
- **Resultado**: Resultados finais e prêmios

### Campos Principais

#### Usuario
- `id`: Identificador único
- `nome`: Nome completo
- `idade`: Idade do participante
- `genero`: Gênero (Feminino, Masculino, etc.)
- `fonte_conhecimento`: Como ficou sabendo da ação
- `data_cadastro`: Data e hora do cadastro

#### Questao
- `id`: Identificador único
- `pergunta`: Texto da pergunta
- `opcao_a`, `opcao_b`, `opcao_c`, `opcao_d`: Opções de resposta
- `resposta_correta`: Letra da resposta correta (A, B, C ou D)

#### Resposta
- `id`: Identificador único
- `usuario_id`: Referência ao usuário
- `questao_id`: Referência à questão
- `resposta_escolhida`: Opção escolhida pelo usuário
- `esta_correta`: Se a resposta está correta
- `data_resposta`: Data e hora da resposta

#### Resultado
- `id`: Identificador único
- `usuario_id`: Referência ao usuário
- `total_acertos`: Número de acertos
- `total_questoes`: Total de questões (sempre 7)
- `ganhou_brinde`: Se ganhou o prêmio
- `data_resultado`: Data e hora do resultado

## 🎯 Fluxo da Aplicação

1. **Tela Inicial**: Boas-vindas e instruções
2. **Cadastro**: Formulário obrigatório com validação
3. **Quiz**: 7 questões sorteadas aleatoriamente
4. **Correção**: Processamento automático das respostas
5. **Resultado**: Exibição da pontuação e prêmios

## 🏆 Sistema de Prêmios

- **Ganha brinde**: Acertos > 3 (mais da metade das 7 questões)
- **Não ganha**: Acertos ≤ 3

## 🎨 Interface

- Design responsivo com Bootstrap 5
- Tema rosa/beauty com gradientes
- Animações suaves e transições
- Ícones Font Awesome
- Loading states e feedback visual

## 🔧 APIs

### POST `/api/cadastrar_usuario`
Cadastra um novo usuário no sistema.

**Body:**
```json
{
    "nome": "Nome Completo",
    "idade": 25,
    "genero": "Feminino",
    "fonte_conhecimento": "Instagram"
}
```

### GET `/api/obter_questoes`
Retorna 7 questões sorteadas aleatoriamente.

### POST `/api/enviar_respostas`
Processa as respostas do usuário.

**Body:**
```json
{
    "respostas": [
        {
            "questao_id": 1,
            "resposta": "A"
        }
    ]
}
```

### GET `/api/obter_resultado`
Retorna o resultado final do usuário.

### POST `/api/limpar_sessao`
Limpa os dados da sessão atual.

## 📊 Relatórios e Estatísticas

O banco de dados permite extrair informações como:
- Total de participantes
- Média de acertos
- Fontes de conhecimento mais populares
- Distribuição por gênero e idade
- Taxa de ganhadores de prêmios

## 🚀 Deploy

### Desenvolvimento
```bash
python app.py
```

### Produção
Para deploy em produção, considere:
- Usar WSGI server (Gunicorn, uWSGI)
- Configurar variáveis de ambiente
- Usar banco de dados PostgreSQL
- Configurar HTTPS
- Implementar logging

## 📝 Licença

Este projeto está sob a licença MIT.

## 👥 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou suporte, entre em contato através dos canais oficiais.
