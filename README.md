# Quiz Beleza sem Fumaça

Um quiz interativo sobre os efeitos do tabagismo na saúde e aparência, desenvolvido em Flask com interface moderna e responsiva.

## 🚀 Funcionalidades

- ✅ Quiz interativo com 50 questões reais sobre tabagismo
- ✅ Interface moderna e responsiva
- ✅ Sistema de cadastro de usuários
- ✅ Armazenamento de respostas e resultados
- ✅ Cálculo automático de pontuação
- ✅ Sistema de brindes baseado no desempenho
- ✅ Design mobile-first

## 🛠️ Tecnologias

- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML5, CSS3, JavaScript, Tailwind CSS
- **Banco de Dados:** SQLite (desenvolvimento) / PostgreSQL (produção)
- **Deploy:** Railway, Render, Heroku, DigitalOcean

## 📋 Pré-requisitos

- Python 3.8+
- pip
- Git

## 🔧 Instalação Local

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/quiz-beleza-que-respira.git
cd quiz-beleza-que-respira
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**
```bash
# Crie um arquivo .env baseado no .env.example
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. **Execute o banco de dados:**
```bash
python app.py
```

6. **Inserir as questões reais:**
```bash
python insert_questions.py
```

7. **Acesse a aplicação:**
```
http://localhost:5000
```

## 🚀 Deploy

### **Render + Railway (Recomendado)**

#### **1. Configurar Banco PostgreSQL no Railway:**
1. Acesse [railway.app](https://railway.app)
2. Clique em "New Project" → "Provision PostgreSQL"
3. Copie a URL de conexão do banco (formato: `postgresql://user:password@host:port/database`)

#### **2. Configurar Aplicação no Render:**
1. Acesse [render.com](https://render.com)
2. Clique em "New +" → "Web Service"
3. Conecte seu repositório GitHub
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn wsgi:app`

#### **3. Variáveis de Ambiente no Render:**
```
DATABASE_URL=postgresql://user:password@host:port/database
SECRET_KEY=sua_chave_secreta_muito_segura_aqui_2024
FLASK_ENV=production
```

#### **4. Deploy:**
- Clique em "Create Web Service"
- Aguarde o build (5-10 minutos)
- Verifique os logs para confirmar que as tabelas foram criadas

### **Verificar Deploy:**
1. **Logs do Render:** Procure por:
   - ✅ "Tabelas criadas com sucesso!"
   - ✅ "Questões inseridas com sucesso!"
   - ✅ "Build successful"

2. **Testar aplicação:**
   - Acesse o URL fornecido pelo Render
   - Complete o quiz para testar o banco

### **Troubleshooting:**
- **Erro de conexão:** Verifique se `DATABASE_URL` está correta
- **Tabelas não criadas:** Verifique os logs do Render
- **Questões não inseridas:** Execute `python init_db.py` localmente primeiro

### **URLs Importantes:**
- **Render:** `https://quiz-beleza-que-respira.onrender.com`
- **Railway:** `https://railway.app/project/[seu-projeto-id]`

### **Opção Alternativa: Railway Completo**

Se preferir usar apenas o Railway:

1. **Criar projeto no Railway:**
   - Acesse [railway.app](https://railway.app)
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"

2. **Configurar PostgreSQL:**
   - Vá em "Variables"
   - Adicione: `DATABASE_URL` (gerado automaticamente)

3. **Configurar variáveis:**
   ```
   FLASK_ENV=production
   SECRET_KEY=sua_chave_secreta_muito_segura
   ```

4. **Deploy automático:**
   - O Railway fará deploy automático a cada push

## 📊 Estrutura do Banco de Dados

### Tabelas:

- **usuarios:** Dados dos participantes
- **questoes:** Banco de 50 questões sobre tabagismo
- **respostas:** Respostas individuais dos usuários
- **resultados:** Resultados finais e prêmios

### Inserir Questões:

```bash
python insert_questions.py
```

## 🔧 Configuração de Produção

### Variáveis de Ambiente Necessárias:

```env
DATABASE_URL=postgresql://user:pass@host:port/db
SECRET_KEY=sua_chave_secreta_muito_segura
FLASK_ENV=production
```

### Configurações de Segurança:

1. **Altere a SECRET_KEY:**
   ```python
   import secrets
   secrets.token_hex(32)
   ```

2. **Configure HTTPS:**
   - Railway e Render já fornecem HTTPS automaticamente

3. **Configure CORS se necessário:**
   ```python
   from flask_cors import CORS
   CORS(app)
   ```

## 📱 Responsividade

O projeto foi desenvolvido com design mobile-first e é totalmente responsivo:

- ✅ Mobile (320px - 768px)
- ✅ Tablet (768px - 1024px)
- ✅ Desktop (1024px+)

## 🎨 Personalização

### Cores do Tema:
```css
--primary: #B67490      /* Rosa principal */
--secondary: #446A46    /* Verde */
--accent: #FFC4DD       /* Rosa claro */
--text-light: #82A284   /* Verde claro */
```

### Fontes:
- Alexandria (Google Fonts)

## 📈 Monitoramento

### Logs:
- Railway: Dashboard integrado
- Render: Logs automáticos
- Heroku: `heroku logs --tail`

### Métricas:
- Acesse `/admin/dados` para ver estatísticas

## 🐛 Troubleshooting

### Problemas Comuns:

1. **Erro de conexão com banco:**
   - Verifique a URL do PostgreSQL
   - Confirme se o banco está ativo

2. **Erro de dependências:**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

3. **Erro de migração:**
   ```bash
   python app.py  # Recria as tabelas
   python insert_questions.py  # Reinsere as questões
   ```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para suporte, envie um email para seu-email@exemplo.com ou abra uma issue no GitHub.

---

**Desenvolvido com ❤️ para conscientização sobre os efeitos do tabagismo**
