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

### Opção 1: Railway (Recomendado)

1. **Crie uma conta no Railway:**
   - Acesse [railway.app](https://railway.app)
   - Faça login com GitHub

2. **Conecte seu repositório:**
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha seu repositório

3. **Configure o banco PostgreSQL:**
   - Vá em "Variables"
   - Adicione: `DATABASE_URL` (será gerado automaticamente)

4. **Configure as variáveis de ambiente:**
   ```
   FLASK_ENV=production
   SECRET_KEY=sua_chave_secreta_muito_segura
   ```

5. **Deploy automático:**
   - O Railway fará deploy automático a cada push

### Opção 2: Render

1. **Crie uma conta no Render:**
   - Acesse [render.com](https://render.com)
   - Faça login com GitHub

2. **Crie um novo Web Service:**
   - Conecte seu repositório
   - Configure:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn wsgi:app`

3. **Configure o banco PostgreSQL:**
   - Crie um novo PostgreSQL database
   - Copie a URL de conexão

4. **Configure as variáveis de ambiente:**
   ```
   DATABASE_URL=sua_url_postgresql
   FLASK_ENV=production
   SECRET_KEY=sua_chave_secreta
   ```

### Opção 3: Heroku

1. **Instale o Heroku CLI:**
```bash
# Windows
winget install --id=Heroku.HerokuCLI

# macOS
brew tap heroku/brew && brew install heroku
```

2. **Faça login:**
```bash
heroku login
```

3. **Crie a aplicação:**
```bash
heroku create seu-quiz-app
```

4. **Configure o PostgreSQL:**
```bash
heroku addons:create heroku-postgresql:mini
```

5. **Configure as variáveis:**
```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=sua_chave_secreta
```

6. **Deploy:**
```bash
git push heroku main
```

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
