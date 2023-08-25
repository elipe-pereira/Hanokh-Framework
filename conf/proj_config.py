#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import configparser

config = configparser.ConfigParser()
BASEPATH = os.environ['PROJ_BASEPATH']
config_file = BASEPATH + "/hanokh.conf"
config.read(config_file)
TEMPLATE_NAME = config.get('hanokh', 'TEMPLATE_NAME')
DOMAIN_BASE_URL = config.get('hanokh', 'DOMAIN_BASE_URL')
DATABASE_ENABLED = config.get('hanokh', 'DATABASE_ENABLED')
DATABASE_TYPE = config.get('hanokh', 'DATABASE_TYPE')
DATABASE_NAME = config.get('hanokh', 'DATABASE_NAME')
DATABASE_USER = config.get('hanokh', 'DATABASE_USER')
DATABASE_PASSWORD = config.get('hanokh', 'DATABASE_PASSWORD')
DATABASE_HOST = config.get('hanokh', 'DATABASE_HOST')
DATABASE_PORT = config.get('hanokh', 'DATABASE_PORT')
DEBUG = config.get('hanokh', 'DEBUG')


def insert_basepath_on_python_path():
    if BASEPATH not in sys.path:
        sys.path.append(BASEPATH)
