#!/usr/bin/python3
# coding: utf-8

# from application.model.debug.log import Log


class User(object):
    def __init__(self):
        # self.debug = Log()
        self.user = ""
        self.password = ""
        # self.debug.log_class("User")

    def set_user(self, user):
        self.user = user
        # self.debug.log_act("self.user", self.user, "set")

    def set_password(self, password):
        self.password = password
        # self.debug.log_act("self.password", self.password, "set")

    def get_user(self):
        # self.debug.log_act("self.user", self.user, "get")
        return self.user

    def get_password(self):
        # self.debug.log_act("self.password", self.password, "get")
        return self.password
