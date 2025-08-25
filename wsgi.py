from app import app, db

# Criar tabelas se não existirem
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
