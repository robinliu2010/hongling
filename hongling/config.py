class BaseConfig(object):
    SECRET_KEY='makesoure to set avery secret-key'

class DevelopmentConfig(BaseConfig):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:618ljj@localhost:3306/hl_database?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs={
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig
}