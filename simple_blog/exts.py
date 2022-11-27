# -*- coding: utf-8 -*- 
"""
Desc: exts模块避免models和__init间的循环依赖，db在这里创建
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()