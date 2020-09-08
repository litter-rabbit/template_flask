import os

base_url = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '')


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(base_url, 'data.db'))


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+://root:root@localhost:3306/databasename?charset=utf8mb4')



class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(base_url, 'data.db'))
    WTF_CSRF_ENABLED = False
    Testing = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
