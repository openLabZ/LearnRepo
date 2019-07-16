#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from web import app
from configs import config
from controllers.main import *


app.config.from_object(config)
db.init_app(app)
