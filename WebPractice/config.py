# -*- encoding: utf-8 -*-

import os

# Debug 开关

# DEBUG = True

# Session & Cookie 相关

SECRET_KEY = os.urandom(24)

# MySQL ORM: SQLAlchemy 相关
HOSTNAME    = '127.0.0.1'
PORT        = '3306'
DATABASE    = 'webflask'
USERNAME    = 'root'
PASSWORD    = 'Root@123'
DB_URI      = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD,
                                                                   HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

