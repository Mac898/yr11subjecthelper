# config.py

class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = 'Blacksheild1'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Blacksheild1@localhost/mac_teachers'

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
