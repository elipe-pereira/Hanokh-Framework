#!/usr/bin/env python3
# coding: utf-8

from app.app_manager import Log
from conf import proj_config as proj
import psycopg2


class Database(object):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("Database")

        self.database_username = proj.DATABASE_USER
        self.debug.log_variable(
            "self.database_username", self.database_username)

        self.database_password = proj.DATABASE_PASSWORD
        self.debug.log_variable(
            "self.database_password", self.database_password)

        self.database_name = proj.DATABASE_NAME
        self.debug.log_variable("self.database_name", self.database_name)

        self.database_host = proj.DATABASE_HOST
        self.debug.log_variable("self.database_host", self.database_host)

        self.database_port = proj.DATABASE_PORT
        self.debug.log_variable("self.database_port", self.database_port)

    def get_database_username(self):
        self.debug.log_act("self.database_username",
                           self.database_username, "get")
        return self.database_username

    def get_database_password(self):
        self.debug.log_act("self.database_password",
                           self.database_password, "get")
        return self.database_password

    def get_database_name(self):
        self.debug.log_act("self.database_name", self.database_name, "get")
        return self.database_name

    def get_database_host(self):
        self.debug.log_act("self.database_host", self.database_host, "get")
        return self.database_host

    def get_database_port(self):
        self.debug.log_act("self.database_port", self.database_port, "get")
        return self.database_port

    def connect_database(self):
        self.debug.log("Criando a conexão com o banco de dados")

        dsn = "dbname=" + self.database_name
        dsn += " user=" + self.database_username
        dsn += " password=" + self.database_password
        dsn += " host=" + self.database_host
        dsn += " port=" + self.database_port

        conn = psycopg2.connect(dsn)

        return conn

    def select_username(self, username):
        sql = """SELECT username, password
                FROM person
                    WHERE username='{0}';""".format(username)

        conn = self.connect_database()
        cur = conn.cursor()

        try:
            self.debug.log("Executando a consulta no banco")
            cur.execute(sql)

        except Exception:
            self.debug.log("Não foi possível conectar ao banco")

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result
