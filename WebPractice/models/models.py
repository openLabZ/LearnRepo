# -*- encoding: utf-8 -*-

# 用于定义与数据库表一一对应的Python模型

from models import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    telephone  = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
