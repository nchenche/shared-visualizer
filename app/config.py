from pathlib import Path
import os


ROOT_PATH =  Path(__file__).parent.parent
APP_PATH = ROOT_PATH / 'app'
STATIC_PATH = APP_PATH / 'static'


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    production=ProductionConfig
)
