# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__, instance_relative_config=True, static_folder='/home/pi/vulnerScan/website/app/static')

from app import views

app.config.from_object('config')