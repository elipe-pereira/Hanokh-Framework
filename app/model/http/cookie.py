#!/usr/bin/env python3
# coding: utf-8

# from app.model.debug.log import Log


class Cookie(object):
    def __init__(self):
        self.ssid = "SSID="
        self.user = "USER="
        # self.debug = Log()
        # self.debug.log_class("Cookie")

    def set_cookie_ssid(self, ssid):
        if ssid:
            self.ssid += ssid
            # self.debug.log_act("self.ssid", self.ssid, "set")

    def set_cookie_user(self, user):
        if user:
            self.user += user.decode()
            # self.debug.log_act("self.user", self.user, set)

    def get_cookie_ssid(self):
        # self.debug.log_act("self.ssid", self.ssid, "get")
        return self.ssid

    def get_cookie_user(self):
        # self.debug.log_act("self.user", self.user, "get")
        return self.user

    def clean_cookie_ssid(self):
        self.ssid = "SSID="
        # self.debug.log_act("self.ssid", self.ssid, "clean")

    def clean_cookie_user(self):
        self.user = "USER="
        # self.debug.log_act("self.user", self.user, "clean")
