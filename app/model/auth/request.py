#!/usr/bin/env python3
# coding: utf-8

from urllib.parse import parse_qs
# from app.model.debug.log import Log


class Request(object):
    def __init__(self, environ, wsgi_input):
        # self.debug = Log()
        # self.debug.log_class("Request")
        self.environ = environ
        self.request = wsgi_input
        self.request = parse_qs(self.request)
        self.username_input = ""
        self.password_input = ""
        self.cookie_request = ""

        try:
            self.cookie_request = self.environ['HTTP_COOKIE'].split(" ")
        except Exception:
            pass

        self.user_cookie = ""
        self.ssid_cookie = ""

    def get_username_input(self):
        try:
            self.username_input = self.request[b'username'][0]
        except:
            # self.debug.log("Não há entrada de login de usuário")
            return False

        if len(self.username_input) > 0:
            # self.debug.log_variable("self.username_input", self.username_input)
            return self.username_input
        else:
            return False

    def get_password_input(self):
        try:
            self.password_input = self.request[b'password'][0]
        except:
            # self.debug.log("Não há entrada de password")
            return False

        if len(self.password_input) > 0:
            # self.debug.log_variable("self.password_input", self.password_input)
            return self.password_input
        else:
            return False

    def get_ssid_cookie_input(self):
        try:
            self.ssid_cookie = parse_qs(self.cookie_request[0])
            self.ssid_cookie = self.ssid_cookie['SSID'][0].strip(";")
        except:
            # self.debug.log("Não há cookie ssid salvo")
            return False

        if len(self.ssid_cookie) > 0:
            # self.debug.log_variable("self.ssid_cookie", self.ssid_cookie)
            return self.ssid_cookie
        else:
            return False

    def get_user_cookie_input(self):
        try:
            self.user_cookie = parse_qs(self.cookie_request[1])
            self.user_cookie = self.user_cookie['USER'][0].strip()
        except:
            # self.debug.log("Não há cookie USER salvo")
            return False

        if len(self.user_cookie) > 0:
            # self.debug.log_variable("self.user_cookie", self.user_cookie)
            return self.user_cookie
        else:
            return False
