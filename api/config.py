import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/examen_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False