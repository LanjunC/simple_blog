# -*- coding: utf-8 -*- 
from flask import Flask
from dotenv import load_dotenv, find_dotenv
from simple_blog.setting import BaseConfig
from simple_blog.exts import *
from simple_blog.models import *
import pymysql
import click
pymysql.install_as_MySQLdb()

load_dotenv(find_dotenv('.env'))

app = Flask(__name__)
app.config.from_object(BaseConfig)
db.init_app(app)
migrate.init_app(app, db)

from simple_blog.commands import * # 后置引入避免__init__和commands的循环依赖
from simple_blog import view
    

