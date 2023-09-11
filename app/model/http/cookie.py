#!/usr/bin/env python3
# coding: utf-8

class Cookie(object):
    def __init__(self):
        self.ssid = "SSID="
        self.user = "USER="

    def set_cookie_ssid(self, ssid):
        if ssid:
            self.ssid += ssid

    def set_cookie_user(self, user):
        if user:
            self.user += user.decode()

    def get_cookie_ssid(self):
        return self.ssid

    def get_cookie_user(self):
        return self.user

    def clean_cookie_ssid(self):
        self.ssid = "SSID="

    def clean_cookie_user(self):
        self.user = "USER="
