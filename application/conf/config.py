#!/usr/bin/python3
# coding: utf-8
from configparser import ConfigParser


class Config:
    def __init__(self):
        self.dbg = None
        self.ip_srv = None
        self.port_srv = None
        self.db_is_enabled = None
        self.db_host = None
        self.db_port = None
        self.db_name = None
        self.db_user = None
        self.db_passwd = None
        self.db_type = None
        self.tpl_name = None
        self.base_uri = None
        self.basepath = None
        self.cfg_file = None
        self.sct_app_name = "app"
        self.sct_server = "server"
        self.parser = ConfigParser()

    def set_basepath(self, basepath):
        self.basepath = basepath

    def get_base_path(self):
        return self.basepath

    def get_template_name(self):
        return self.tpl_name

    def get_base_uri(self):
        return self.base_uri

    def get_database_is_enabled(self):
        return self.db_is_enabled

    def get_db_type(self):
        return self.db_type

    def get_db_name(self):
        return self.db_name

    def get_db_user(self):
        return self.db_user

    def get_db_passwd(self):
        return self.db_passwd

    def get_db_host(self):
        return self.db_host

    def get_db_port(self):
        return self.db_port

    def get_ip_srv(self):
        return self.ip_srv

    def get_port_srv(self):
        return self.port_srv

    def get_debug(self):
        return self.dbg

    def read_settings(self):
        self.cfg_file = self.basepath + "/conf/app.conf"
        self.parser.read(self.cfg_file)
        self.tpl_name = self.parser.get(self.sct_app_name, 'tpl_name')
        self.base_uri = self.parser.get(self.sct_app_name, 'base_url')
        self.db_is_enabled = self.parser.get(self.sct_app_name, 'db_enabled')
        self.db_type = self.parser.get(self.sct_app_name, 'db_type')
        self.db_name = self.parser.get(self.sct_app_name, 'db_name')
        self.db_user = self.parser.get(self.sct_app_name, 'db_user')
        self.db_passwd = self.parser.get(self.sct_app_name, 'db_password')
        self.db_host = self.parser.get(self.sct_app_name, 'db_host')
        self.db_port = self.parser.get(self.sct_app_name, 'db_port')
        self.ip_srv = self.parser.get(self.sct_server, 'host')
        self.port_srv = int(self.parser.get(self.sct_server, 'port'))
