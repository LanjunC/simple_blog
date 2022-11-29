# -*- coding: utf-8 -*-
import os

DATABASE_USER = os.getenv('DATABASE_USER', 'root')
DATABASE_PWD = os.getenv('DATABASE_PWD')


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@127.0.0.1/blog?charset=utf8mb4'.format(
        DATABASE_USER, DATABASE_PWD)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SIMPLE_BLOG_PER_PAGE = 3
    
