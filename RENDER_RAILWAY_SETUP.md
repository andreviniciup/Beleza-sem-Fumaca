# 🚀 Configuração Render + Railway

## 📋 **Pré-requisitos**

- ✅ Conta no [Render.com](https://render.com)
- ✅ Conta no [Railway.app](https://railway.app)
- ✅ Projeto no GitHub

## 🔧 **Passo 1: Configurar Banco PostgreSQL no Railway**

### **1.1 Criar Projeto no Railway**
1. Acesse [railway.app](https://railway.app)
2. Clique em **"New Project"**
3. Selecione **"Provision PostgreSQL"**

### **1.2 Obter URL do Banco**
1. Clique no banco PostgreSQL criado
2. Vá na aba **"Connect"**
3. Copie a **"Postgres Connection URL"**
4. Formato: `postgresql://user:password@host:port/database`

## 🔧 **Passo 2: Configurar Aplicação no Render**

### **2.1 Criar Web Service**
1. Acesse [render.com](https://render.com)
2. Clique em **"New +"** → **"Web Service"**
3. Conecte seu repositório GitHub
4. Selecione o repositório do quiz

### **2.2 Configurações do Render**

#### **Nome do Serviço:**
```
quiz-beleza-que-respira
```

#### **Environment:**
```
Python 3
```

#### **Build Command:**
```bash
pip install -r requirements.txt
```

#### **Start Command:**
```bash
gunicorn wsgi:app
```

### **2.3 Variáveis de Ambiente**

Clique em **"Environment"** e adicione:

#### **DATABASE_URL:**
```
Cole aqui a URL do PostgreSQL do Railway
```

#### **SECRET_KEY:**
```
sua_chave_secreta_muito_segura_aqui_2024
```

#### **FLASK_ENV:**
```
production
```

## 🔧 **Passo 3: Configurações Avançadas**

### **3.1 Health Check Path:**
```
/
```

### **3.2 Auto-Deploy:**
```
✅ Enabled
```

## 🚀 **Passo 4: Deploy**

### **4.1 Primeiro Deploy**
1. Clique em **"Create Web Service"**
2. Aguarde o build (pode demorar 5-10 minutos)
3. Verifique os logs para erros

### **4.2 Verificar Logs**
1. Vá na aba **"Logs"**
2. Procure por:
   - ✅ "Tabelas criadas com sucesso!"
   - ✅ "Questões inseridas com sucesso!"
   - ✅ "Build successful"

## 🐛 **Troubleshooting**

### **Erro: psycopg2 não encontrado**
**Solução:** Verifique se `psycopg2-binary==2.9.7` está no `requirements.txt`

### **Erro: DATABASE_URL não encontrada**
**Solução:** Verifique se a variável `DATABASE_URL` está configurada no Render

### **Erro: Conexão com banco falhou**
**Solução:** Verifique se a URL do Railway está correta

### **Erro: Tabelas não criadas**
**Solução:** Verifique os logs do Render para ver se `db.create_all()` executou

## ✅ **Checklist de Verificação**

### **Railway:**
- [ ] Projeto PostgreSQL criado
- [ ] URL do banco copiada
- [ ] Banco está ativo

### **Render:**
- [ ] Web Service criado
- [ ] Repositório conectado
- [ ] Build Command configurado
- [ ] Start Command configurado
- [ ] Variáveis de ambiente configuradas
- [ ] Deploy executado com sucesso

### **Aplicação:**
- [ ] Tabelas criadas (verificar logs)
- [ ] Questões inseridas (verificar logs)
- [ ] Aplicação responde no URL do Render

## 🔗 **URLs Importantes**

### **Render:**
```
https://quiz-beleza-que-respira.onrender.com
```

### **Railway Dashboard:**
```
https://railway.app/project/[seu-projeto-id]
```

## 📊 **Monitoramento**

### **Render Dashboard:**
- Verificar status do serviço
- Monitorar logs em tempo real
- Verificar uso de recursos

### **Railway Dashboard:**
- Verificar conexões do banco
- Monitorar uso de dados
- Verificar logs do PostgreSQL

## 🎉 **Resultado Final**

Após a configuração, você terá:
- ✅ **Aplicação rodando** no Render
- ✅ **Banco PostgreSQL** no Railway
- ✅ **Deploy automático** quando fizer push
- ✅ **URL pública** para acessar o quiz
- ✅ **Banco de dados** persistente

## 🚀 **Próximos Passos**

1. **Teste a aplicação** no URL do Render
2. **Verifique se os sons funcionam**
3. **Teste no celular** para autoplay
4. **Monitore os logs** para problemas
5. **Configure domínio personalizado** (opcional)
