# 🔧 Solução para Python 3.13 + psycopg2

## 🚨 **Problema:**
```
ImportError: undefined symbol: _PyInterpreterState_Get
```

Este erro acontece porque `psycopg2-binary==2.9.7` não é compatível com Python 3.13.

## ✅ **Soluções Implementadas:**

### **1. Atualização do psycopg2**
- ✅ Atualizado para `psycopg2-binary==2.9.9`
- ✅ Mais compatível com Python 3.13

### **2. Fallback para SQLite**
- ✅ Se PostgreSQL falhar, usa SQLite automaticamente
- ✅ Aplicação continua funcionando

### **3. Runtime.txt**
- ✅ Força Python 3.11.7 (mais estável)
- ✅ Evita problemas de compatibilidade

## 🚀 **Configuração no Render:**

### **Opção 1: Usar Python 3.11 (Recomendado)**

1. **No Render, configure:**
   - **Environment Variables:**
     ```
     PYTHON_VERSION=3.11.7
     ```

2. **Ou use o arquivo `runtime.txt`:**
   ```
   python-3.11.7
   ```

### **Opção 2: Usar SQLite (Fallback)**

Se PostgreSQL continuar com problemas:

1. **Mude o Build Command para:**
   ```bash
   pip install -r requirements-sqlite.txt
   ```

2. **Remova a variável `DATABASE_URL`**
   - A aplicação usará SQLite automaticamente

### **Opção 3: Atualizar psycopg2**

1. **No `requirements.txt`:**
   ```
   psycopg2-binary==2.9.9
   ```

2. **Ou usar versão mais recente:**
   ```
   psycopg2-binary==2.9.10
   ```

## 🔧 **Configurações no Render:**

### **Build Command:**
```bash
pip install -r requirements.txt
```

### **Start Command:**
```bash
gunicorn wsgi:app
```

### **Environment Variables:**
```
PYTHON_VERSION=3.11.7
SECRET_KEY=sua_chave_secreta_muito_segura_aqui_2024
FLASK_ENV=production
DATABASE_URL=postgresql://user:password@host:port/database
```

## 🐛 **Troubleshooting:**

### **Se ainda der erro:**
1. **Remova `DATABASE_URL`** - usará SQLite
2. **Use `requirements-sqlite.txt`** - sem PostgreSQL
3. **Force Python 3.11** - mais estável

### **Para verificar logs:**
1. Vá na aba **"Logs"** do Render
2. Procure por:
   - ✅ "Tabelas criadas com sucesso!"
   - ✅ "Questões inseridas com sucesso!"
   - ⚠️ "Usando SQLite como fallback"

## ✅ **Checklist:**

- [ ] `runtime.txt` configurado para Python 3.11.7
- [ ] `psycopg2-binary==2.9.9` no requirements.txt
- [ ] Variáveis de ambiente configuradas
- [ ] Build Command correto
- [ ] Start Command correto

## 🎉 **Resultado:**

Após as correções:
- ✅ **Aplicação roda** no Python 3.11
- ✅ **PostgreSQL funciona** ou fallback para SQLite
- ✅ **Deploy bem-sucedido** no Render
- ✅ **Quiz funcionando** em produção
