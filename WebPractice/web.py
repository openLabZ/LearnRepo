#!/usr/bin/python3
# -*- encoding: utf-8 -*-


from flask import Flask, render_template, request, redirect, url_for
from exts import db
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return redirect(url_for('register'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000')
