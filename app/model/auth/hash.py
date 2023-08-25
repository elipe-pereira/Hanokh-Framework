#!/usr/bin/env python3
# coding: utf-8

from app.application import Database
from app.application import Log
import hashlib


class Hash(object):
    def __init__(self):
        self.hash = ""
        self.user = ""
        self.db = Database()
        self.db_search = ""
        self.debug = Log()
        self.debug.log_class("Hash")

    def set_hash(self, user, password):
        join_user_pass = user + password
        if join_user_pass:
            self.debug.log_act("self.hash", self.hash, "set")
            self.hash = hashlib.sha512(join_user_pass).hexdigest()
        else:
            self.hash = False

    def get_hash(self):
        self.debug.log_act("self.hash", self.hash, "get")
        return self.hash

    def get_hash_on_database(self, user):
        self.user = user
        self.db_search = self.db.select_username(self.user)

        self.debug.log_act("self.db_search", self.db_search, "get")

        if self.db_search:
            self.hash = self.db_search[1]
            return self.hash
        else:
            return False

    def is_valid_user_hash(self, ssid, ssid_on_db):
        if ssid is False and ssid_on_db is False:
            self.debug.log("Não há usuário válido")
            return False
        elif ssid == ssid_on_db:
            self.debug.log("Usuário válido")
            return True
        else:
            return False
