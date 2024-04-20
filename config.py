import os 

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
class Config():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'loginform_datatable'