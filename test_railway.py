#!/usr/bin/env python3
"""
Script para testar configuração Railway localmente
"""

import os
from app import app, db, Questao

def test_railway_config():
    """Testa a configuração do Railway"""
    
    print("🔍 Testando configuração Railway...")
    
    with app.app_context():
        try:
            # Verificar configuração do banco
            db_uri = app.config['SQLALCHEMY_DATABASE_URI']
            print(f"📊 URI do banco: {db_uri}")
            
            # Testar conexão
            db.engine.execute('SELECT 1')
            print("✅ Conexão com banco estabelecida!")
            
            # Verificar se as tabelas existem
            tables = db.engine.table_names()
            print(f"📋 Tabelas encontradas: {tables}")
            
            # Verificar questões
            questao_count = Questao.query.count()
            print(f"📝 Questões no banco: {questao_count}")
            
            if questao_count == 0:
                print("⚠️ Nenhuma questão encontrada!")
                print("💡 Execute: python insert_questions.py")
            else:
                print("✅ Questões carregadas com sucesso!")
                
        except Exception as e:
            print(f"❌ Erro na configuração: {str(e)}")
            print("\n🔧 Possíveis soluções:")
            print("1. Verifique se DATABASE_URL está configurada")
            print("2. Verifique se o banco PostgreSQL está ativo")
            print("3. Verifique se as credenciais estão corretas")

def test_environment():
    """Testa as variáveis de ambiente"""
    
    print("\n🔧 Verificando variáveis de ambiente...")
    
    # Verificar DATABASE_URL
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        print(f"✅ DATABASE_URL: {database_url[:50]}...")
    else:
        print("⚠️ DATABASE_URL não encontrada")
    
    # Verificar SECRET_KEY
    secret_key = os.environ.get('SECRET_KEY')
    if secret_key:
        print(f"✅ SECRET_KEY: {secret_key[:20]}...")
    else:
        print("⚠️ SECRET_KEY não encontrada")
    
    # Verificar FLASK_ENV
    flask_env = os.environ.get('FLASK_ENV')
    if flask_env:
        print(f"✅ FLASK_ENV: {flask_env}")
    else:
        print("⚠️ FLASK_ENV não encontrada")

if __name__ == "__main__":
    test_environment()
    test_railway_config()
