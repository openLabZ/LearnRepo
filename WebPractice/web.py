#!/usr/bin/python3
# -*- encoding: utf-8 -*-


from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    return 'My Web Page Practice from zhcc.'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000')
