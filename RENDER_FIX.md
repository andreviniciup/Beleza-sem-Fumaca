# 🔧 Solução para Erro de Deploy no Render

## 🚨 Problema Identificado

O erro "Exited with status 1" geralmente indica problemas de configuração ou dependências.

## ✅ Soluções Passo a Passo

### 1. **Configuração no Render Dashboard**

1. **Acesse seu projeto no Render**
2. **Vá em "Environment"**
3. **Configure estas variáveis:**

```env
FLASK_ENV=production
SECRET_KEY=0c1725a412c44bf9556bca61f746faa0f5f90af4fe76dc286dbad0bc727f827f
DATABASE_URL=sua_url_do_railway_postgresql
```

### 2. **Configuração do Build**

1. **Build Command:**
```bash
pip install -r requirements.txt
```

2. **Start Command:**
```bash
gunicorn wsgi:app
```

### 3. **Verificar Logs**

1. **No Render, vá em "Logs"**
2. **Procure por erros específicos**
3. **Copie os logs de erro para análise**

### 4. **Possíveis Problemas e Soluções**

#### **Problema 1: Dependências não encontradas**
```bash
# Verifique se requirements.txt tem:
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
psycopg2-binary==2.9.7
python-dotenv==1.0.0
gunicorn==21.2.0
```

#### **Problema 2: Erro de importação**
- Verifique se todos os arquivos estão no repositório
- Confirme se `wsgi.py` está na raiz

#### **Problema 3: Erro de banco de dados**
- Verifique se a `DATABASE_URL` está correta
- Confirme se o PostgreSQL do Railway está ativo

### 5. **Teste Local**

Antes do deploy, teste localmente:

```bash
# Instalar dependências
pip install -r requirements.txt

# Testar se o app roda
python wsgi.py

# Testar gunicorn
gunicorn wsgi:app
```

### 6. **Deploy Manual**

Se o deploy automático falhar:

1. **Force um novo deploy**
2. **Verifique os logs em tempo real**
3. **Corrija os erros identificados**

### 7. **Verificação Final**

Após o deploy bem-sucedido:

1. **Acesse a URL do app**
2. **Teste o fluxo completo**
3. **Execute o script de questões:**

```bash
# No terminal do Render (se disponível)
python init_db.py
```

## 🐛 Troubleshooting Específico

### **Erro: "Module not found"**
```bash
# Adicione ao requirements.txt:
Werkzeug==2.3.7
```

### **Erro: "Database connection failed"**
- Verifique a URL do PostgreSQL
- Confirme se o banco está acessível
- Teste a conexão localmente

### **Erro: "Application failed to start"**
- Verifique se `wsgi.py` está correto
- Confirme se `gunicorn` está instalado
- Teste o comando de start localmente

## 📞 Próximos Passos

1. **Aplique as correções acima**
2. **Faça um novo deploy**
3. **Monitore os logs**
4. **Teste a aplicação**

Se o problema persistir, compartilhe os logs de erro específicos para análise detalhada.
