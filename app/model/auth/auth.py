#!/usr/bin/python3
# coding: utf-8

# from app.model.debug.log import Log
from app.model.auth.hash import Hash
from app.model.http.cookie import Cookie


class Auth:
    def __init__(self, base_path, config, header, status, auth_request):
        self.base_path = base_path
        self.config = config
        self.auth_request = auth_request
        self.hash = Hash(self.base_path, self.config)
        self.header = header
        self.status = status
        self.user_input = ""
        self.pass_input = ""
        self.hash_access_input = ""
        self.valid_user_hash = ""
        self.cookie = Cookie()
        self.ssid = ""
        self.user_cookie = ""
        self.ssid_on_db = ""
        self.is_ssid_valid = ""

    def is_auth(self):
        self.user_cookie = self.auth_request.get_user_cookie_input()

        self.ssid = self.auth_request.get_ssid_cookie_input()

        self.ssid_on_db = self.hash.get_hash_on_database(self.user_cookie)

        self.is_ssid_valid = self.hash.is_valid_user_hash(
            self.ssid, self.ssid_on_db)

        if self.is_ssid_valid:
            return True
        else:
            self.user_input = self.auth_request.get_username_input()

            self.pass_input = self.auth_request.get_password_input()

            self.hash.set_hash(self.user_input, self.pass_input)
            self.ssid = self.hash.get_hash()

            if self.user_input:
                self.ssid_on_db = self.hash.get_hash_on_database(
                    self.user_input.decode())

            self.is_ssid_valid = self.hash.is_valid_user_hash(
              self.ssid, self.ssid_on_db)

            if self.is_ssid_valid:
                self.cookie.set_cookie_ssid(self.ssid)
                self.cookie.set_cookie_user(self.user_input)

                self.header.set_header([
                    ('Content-Type', 'text/html'),
                    ('set-cookie', self.cookie.get_cookie_ssid()),
                    ('set-cookie', self.cookie.get_cookie_user())
                ])
                self.status.set_status("200 OK")

                return True
            else:
                self.cookie.clean_cookie_ssid()
                self.cookie.clean_cookie_user()

                self.header.set_header([
                    ('Content-Type', 'text/html'),
                    ('set-cookie', self.cookie.get_cookie_ssid()),
                    ('set-cookie', self.cookie.get_cookie_user())
                    ])
                self.status.set_status("200 OK")

                return False
