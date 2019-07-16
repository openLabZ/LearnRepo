#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from flask import render_template, request, redirect, url_for, session
from controllers import app
from models.models import db, User
from sqlalchemy import and_


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        checkbox = request.form.get('checkbox')

        user = User.query.filter(and_(User.telephone == telephone,
                                      User.password == password)).first()
        if user:
            session['telephone'] = telephone
            if checkbox:
                session.permanent = True
                print('[Info] set session permanent = true!')
            return redirect(url_for('index'))
        else:
            print('[Info] 用户名或密码错误！')
            return redirect(url_for('main.login'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone == telephone).first()

        if user:
            return '用户已存在！请重新注册！'
        else:
            if password1 != password2:
                return '两次密码输入不一致，请确认后再重新注册！'
            else:
                session['telephone'] = telephone
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('main.index'))
