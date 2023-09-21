#!/usr/bin/env python3
# coding: utf-8

import hashlib
from application.db.database import Database


class Hash(object):
    def __init__(self, base_path, config):
        self.base_path = base_path
        self.config = config
        self.hash = ""
        self.user = ""
        self.db = Database(self.base_path, self.config)
        self.db_search = ""

    def set_hash(self, user, password):
        join_user_pass = user + password
        if join_user_pass:
            self.hash = hashlib.sha512(join_user_pass).hexdigest()
        else:
            self.hash = False

    def get_hash(self):
        return self.hash

    def get_hash_on_database(self, user):
        self.user = user
        self.db_search = self.db.select_username(self.user)

        if self.db_search:
            self.hash = self.db_search[1]
            return self.hash
        else:
            return False

    def is_valid_user_hash(self, ssid, ssid_on_db):
        if ssid is False and ssid_on_db is False:
            return False
        elif ssid == ssid_on_db:
            return True
        else:
            return False
