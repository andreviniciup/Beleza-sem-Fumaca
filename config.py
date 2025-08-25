import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua_chave_secreta_aqui_mude_para_producao'
    
    # Configuração do banco de dados - PostgreSQL para Railway, SQLite para desenvolvimento
    @staticmethod
    def get_database_uri():
        # Verificar se tem DATABASE_URL (Railway/Produção)
        database_url = os.environ.get('DATABASE_URL')
        if database_url:
            try:
                # Railway usa postgres://, mas SQLAlchemy precisa postgresql://
                if database_url.startswith('postgres://'):
                    database_url = database_url.replace('postgres://', 'postgresql://', 1)
                print("🔄 PostgreSQL detectado - usando banco de produção")
                return database_url
            except Exception as e:
                print(f"⚠️ Erro ao configurar PostgreSQL: {e}")
                print("🔄 Usando SQLite como fallback")
                return 'sqlite:///quiz.db'
        
        # Fallback para SQLite (desenvolvimento)
        print("🔄 Usando SQLite para desenvolvimento")
        return 'sqlite:///quiz.db'
    
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
