class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///soft_toys_db.db'


class DevelopmentConfig(Config):
    DEBUG = True
    REPOSITORY = 'memory'
    ENV = 'development'


class ProductionConfig(Config):
    DEBUG = False
    REPOSITORY = 'sqlite'
    ENV = 'production'
