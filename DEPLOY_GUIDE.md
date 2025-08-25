# 🚀 Guia Rápido de Deploy

## 📋 Pré-requisitos

1. **Conta no GitHub** com o projeto enviado
2. **Conta no Railway** (gratuita)
3. **Projeto configurado** com todos os arquivos

## 🎯 Deploy no Railway (Recomendado)

### Passo 1: Preparar o Projeto

1. **Certifique-se de que todos os arquivos estão no GitHub:**
   ```bash
   git add .
   git commit -m "Preparando para deploy"
   git push origin main
   ```

2. **Verifique se estes arquivos estão no repositório:**
   - ✅ `requirements.txt`
   - ✅ `wsgi.py`
   - ✅ `Procfile`
   - ✅ `config.py`
   - ✅ `app.py`
   - ✅ `insert_questions.py`

### Passo 2: Criar Projeto no Railway

1. **Acesse [railway.app](https://railway.app)**
2. **Faça login com GitHub**
3. **Clique em "New Project"**
4. **Selecione "Deploy from GitHub repo"**
5. **Escolha seu repositório**

### Passo 3: Configurar Banco de Dados

1. **No dashboard do Railway, clique em "New"**
2. **Selecione "Database" → "PostgreSQL"**
3. **Aguarde a criação do banco**
4. **Copie a URL de conexão**

### Passo 4: Configurar Variáveis de Ambiente

1. **No seu projeto, vá em "Variables"**
2. **Adicione estas variáveis:**

```env
DATABASE_URL=sua_url_postgresql_aqui
FLASK_ENV=production
SECRET_KEY=sua_chave_secreta_muito_segura_aqui
```

3. **Para gerar uma SECRET_KEY segura:**
   ```python
   import secrets
   print(secrets.token_hex(32))
   ```

### Passo 5: Deploy Automático

1. **O Railway fará deploy automático**
2. **Aguarde a conclusão do build**
3. **Clique no domínio gerado para acessar**

### Passo 6: Inserir Questões

1. **Acesse o terminal do Railway:**
   - Vá em "Deployments" → "Latest" → "View Logs"
   - Clique em "Open Shell"

2. **Execute o script de questões:**
   ```bash
   python insert_questions.py
   ```

## 🔧 Configurações Alternativas

### Render

1. **Acesse [render.com](https://render.com)**
2. **Crie um "Web Service"**
3. **Conecte seu repositório GitHub**
4. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn wsgi:app`
5. **Adicione PostgreSQL database**
6. **Configure as variáveis de ambiente**

### Heroku

1. **Instale Heroku CLI**
2. **Faça login:** `heroku login`
3. **Crie app:** `heroku create seu-app-name`
4. **Adicione PostgreSQL:** `heroku addons:create heroku-postgresql:mini`
5. **Configure variáveis:**
   ```bash
   heroku config:set FLASK_ENV=production
   heroku config:set SECRET_KEY=sua_chave_secreta
   ```
6. **Deploy:** `git push heroku main`

## 🐛 Troubleshooting

### Erro: "No module named 'psycopg2'"
```bash
# Adicione ao requirements.txt:
psycopg2-binary==2.9.7
```

### Erro: "Database connection failed"
- Verifique se a `DATABASE_URL` está correta
- Confirme se o banco PostgreSQL está ativo

### Erro: "Application error"
- Verifique os logs no dashboard
- Confirme se todas as variáveis estão configuradas

### Erro: "Module not found"
```bash
# Verifique se requirements.txt tem:
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
psycopg2-binary==2.9.7
python-dotenv==1.0.0
gunicorn==21.2.0
```

## 📊 Verificar Funcionamento

1. **Acesse a URL do seu app**
2. **Teste o fluxo completo:**
   - Página inicial
   - Formulário de cadastro
   - Quiz com questões
   - Resultado final

3. **Verifique os dados:**
   - Acesse `/admin/dados` para ver estatísticas

## 🔒 Segurança

1. **Altere a SECRET_KEY** para produção
2. **Configure HTTPS** (Railway/Render já fornecem)
3. **Monitore os logs** regularmente
4. **Faça backup** do banco de dados

## 📈 Monitoramento

### Railway
- Dashboard integrado com logs
- Métricas de uso
- Deploy automático

### Render
- Logs em tempo real
- Métricas de performance
- Health checks

### Heroku
```bash
heroku logs --tail
heroku ps
```

## 🎉 Sucesso!

Seu quiz está online e funcionando! 🚀

**URL:** https://seu-app.railway.app

**Próximos passos:**
1. Teste todas as funcionalidades
2. Configure domínio personalizado (opcional)
3. Monitore o uso e performance
4. Faça backup regular dos dados

---

**Precisa de ajuda?** Abra uma issue no GitHub ou consulte a documentação da plataforma escolhida.
