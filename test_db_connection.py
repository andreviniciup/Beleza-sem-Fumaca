#!/usr/bin/env python3
"""
Script para testar conexão com banco de dados
"""

import os
from app import app, db, Questao

def test_database_connection():
    """Testa a conexão com o banco de dados"""
    
    print("🔍 Testando conexão com banco de dados...")
    
    with app.app_context():
        try:
            # Testar conexão
            db.engine.execute('SELECT 1')
            print("✅ Conexão com banco estabelecida!")
            
            # Verificar se as tabelas existem
            tables = db.engine.table_names()
            print(f"📊 Tabelas encontradas: {tables}")
            
            # Verificar questões
            questao_count = Questao.query.count()
            print(f"📝 Questões no banco: {questao_count}")
            
            if questao_count == 0:
                print("⚠️ Nenhuma questão encontrada!")
                print("💡 Execute: python init_db.py")
            else:
                print("✅ Questões carregadas com sucesso!")
                
        except Exception as e:
            print(f"❌ Erro na conexão: {str(e)}")
            print("\n🔧 Possíveis soluções:")
            print("1. Verifique se DATABASE_URL está configurada")
            print("2. Verifique se o banco PostgreSQL está ativo")
            print("3. Verifique se as credenciais estão corretas")

if __name__ == "__main__":
    test_database_connection()
