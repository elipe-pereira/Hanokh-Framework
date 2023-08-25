#!/usr/bin/python3
# coding: utf-8

from app.application import Hash
from app.application import Cookie
from app.application import Log


class Auth(object):
    def __init__(self, header, request):
        self.request = request
        self.hash = Hash()
        self.header = header
        self.user_input = ""
        self.pass_input = ""
        self.hash_access_input = ""
        self.valid_user_hash = ""
        self.cookie = Cookie()
        self.ssid = ""
        self.user_cookie = ""
        self.ssid_on_db = ""
        self.is_ssid_valid = ""
        self.debug = Log()
        self.debug.log_class("Auth")

    def is_auth(self):
        self.user_cookie = self.request.get_user_cookie_input()
        self.debug.log_variable("self.user_cookie", self.user_cookie)

        self.ssid = self.request.get_ssid_cookie_input()
        self.debug.log_variable("self.ssid", self.ssid)

        self.ssid_on_db = self.hash.get_hash_on_database(self.user_cookie)
        self.debug.log_variable("self.ssid_on_db", self.ssid_on_db)

        self.is_ssid_valid = self.hash.is_valid_user_hash(
            self.ssid, self.ssid_on_db)
        self.debug.log_variable("self.is_ssid_valid", self.is_ssid_valid)

        if self.is_ssid_valid:
            return True
        else:
            self.user_input = self.request.get_username_input()
            self.debug.log_variable("self.user_input", self.user_input)

            self.pass_input = self.request.get_password_input()
            self.debug.log_variable("self.pass_input", self.pass_input)

            self.hash.set_hash(self.user_input, self.pass_input)
            self.ssid = self.hash.get_hash()
            self.debug.log_variable("self.ssid", self.ssid)

            if self.user_input:
                self.ssid_on_db = self.hash.get_hash_on_database(
                    self.user_input.decode())
                self.debug.log_variable("self.ssid_on_db", self.ssid_on_db)

            self.is_ssid_valid = self.hash.is_valid_user_hash(
              self.ssid, self.ssid_on_db)
            self.debug.log_variable("self.is_ssid_valid", self.is_ssid_valid)

            if self.is_ssid_valid:
                self.cookie.set_cookie_ssid(self.ssid)
                self.cookie.set_cookie_user(self.user_input)

                self.header.set_header([
                    ('Content-Type', 'text/html'),
                    ('set-cookie', self.cookie.get_cookie_ssid()),
                    ('set-cookie', self.cookie.get_cookie_user())
                ])

                return True
            else:
                self.cookie.clean_cookie_ssid()
                self.cookie.clean_cookie_user()

                self.header.set_header([
                    ('Content-Type', 'text/html'),
                    ('set-cookie', self.cookie.get_cookie_ssid()),
                    ('set-cookie', self.cookie.get_cookie_user())
                    ])

                return False
