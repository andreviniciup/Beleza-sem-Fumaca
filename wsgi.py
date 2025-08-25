from app import app, db, Questao

# Criar tabelas e inserir dados se necessário
with app.app_context():
    try:
        # Criar tabelas
        db.create_all()
        print("✅ Tabelas criadas com sucesso!")
        
        # Verificar se já existem questões
        if Questao.query.count() == 0:
            print("📝 Inserindo questões...")
            from insert_questions import insert_real_questions
            insert_real_questions()
            print("✅ Questões inseridas com sucesso!")
        else:
            print(f"📊 Já existem {Questao.query.count()} questões no banco")
            
    except Exception as e:
        print(f"⚠️ Erro ao inicializar banco: {e}")
        print("🔄 Tentando continuar com SQLite...")

if __name__ == "__main__":
    app.run()
