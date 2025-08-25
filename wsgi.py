from app import app, db, Questao

# Criar tabelas e inserir dados se necessário
with app.app_context():
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

if __name__ == "__main__":
    app.run()
