import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False