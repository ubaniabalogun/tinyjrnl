"""
Configuration Class
"""
import os

class Config(object):
    """
    Base configuration class
    """
    pass

class DevConfig(Config):
    """
    Development Configurations
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/tinyjrnl.db'.format(os.path.dirname(os.path.realpath(__file__)))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class ProdConfig(Config):
    """
    Production Configurations
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/tinyjrnl.db'.format(os.path.dirname(os.path.realpath(__file__)))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
