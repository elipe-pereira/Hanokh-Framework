#!/usr/bin/env python3
# coding: utf-8

import psycopg2


class Database(object):
    def __init__(self, base_path, config):
        self.base_path = base_path
        self.config = config
        self.database_username = self.config.get_db_user()
        self.database_password = self.config.get_db_passwd()
        self.database_name = self.config.get_db_name()
        self.database_host = self.config.get_db_host()
        self.database_port = self.config.get_db_port()

    def get_database_username(self):
        return self.database_username

    def get_database_password(self):
        return self.database_password

    def get_database_name(self):
        return self.database_name

    def get_database_host(self):
        return self.database_host

    def get_database_port(self):
        return self.database_port

    def connect_database(self):
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
            cur.execute(sql)
        except Exception:
            pass

        result = cur.fetchone()

        cur.close()
        conn.close()

        return result
