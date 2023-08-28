#!/usr/bin/python3
# coding: utf-8
from configparser import ConfigParser
from app.model.conf.database_config import DatabaseConfig
from app.model.conf.server_config import ServerConfig


class Config:
    def __init__(self, base_path):
        self.base_path = base_path
        self.parser = ConfigParser()
        self.config_file = ""
        self.template_name = ""
        self.base_uri = ""
        self.server_conf = ServerConfig()
        self.database_conf = DatabaseConfig()
        self.database_is_enabled = ""
        self.database_type = ""
        self.database_name = ""
        self.database_user = ""
        self.database_password = ""
        self.database_host = ""
        self.database_port = ""
        self.debug = ""

    def get_base_path(self):
        return self.base_path

    def set_template_name(self, template_name):
        self.template_name = template_name

    def get_template_name(self):
        return self.template_name

    def set_base_uri(self, base_uri):
        self.base_uri = base_uri

    def get_base_uri(self):
        return self.base_uri

    def set_database_is_enabled(self, database_is_enabled):
        self.database_is_enabled = database_is_enabled

    def get_database_is_enabled(self):
        return self.database_is_enabled

    def set_debug(self, debug):
        self.debug = debug

    def get_debug(self):
        return self.debug

    def read_config_file(self):
        pass
