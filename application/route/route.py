#!/usr/bin/env python3
# coding: utf-8

from application.pages.auth import Auth
from application.pages.start import Start
from application.pages.login import Login
from application.http.cookie import Cookie
from application.conf.config import Config
from application.pages.error_404 import Error404


class Route:
    def __init__(self, base_path, header, status, is_auth=False):
        self.header = header
        self.status = status
        self.is_auth = is_auth
        self.base_path = base_path
        self.html_page = ""
        self.json_page = ""
        self.path = ""
        self.auth_routes_html = {
            '/': Start,
            '/login': Login,
            '/auth': Auth,
            '/404': Error404
        }
        self.unauth_routes_html = {
            '/': Start,
            '/auth': Auth,
            '/login': Login,
            '/404': Error404,
            '/start': Start
        }
        self.auth_routes_json = {}
        self.unauth_routes_json = {}
        self.cookie = Cookie()
        self.config = Config()
        self.config.set_base_path(self.base_path)
        self.config.read_settings()

    def get_auth_routes_html(self):
        return self.auth_routes_html

    def get_unauth_routes_html(self):
        return self.unauth_routes_html

    def get_auth_routes_json(self):
        return self.auth_routes_json

    def get_unauth_routes_json(self):
        return self.unauth_routes_json

    def get_route(self, path):
        self.path = path
        if self.is_auth:
            if self.path in self.auth_routes_html:
                self.html_page = self.auth_routes_html[self.path]
                if self.path == "/auth":
                    self.html_page = self.html_page(self.base_path, self.config, self.is_auth).load()
                elif self.path == "/login":
                    self.cookie.clean_cookie_ssid()
                    self.cookie.clean_cookie_user()
                    self.status.set_status("200 OK")
                    self.header.set_header([
                        ('Content-type', 'text/html'),
                        ('set-cookie', self.cookie.get_cookie_ssid()),
                        ('set-cookie', self.cookie.get_cookie_user())

                    ])
                    self.html_page = self.html_page(self.base_path, self.config).load()
                else:
                    self.header.set_header([('Content-type', 'text/html')])
                    self.status.set_status("200 OK")
                    self.html_page = self.html_page(self.base_path, self.config).load()

                return self.html_page
            else:
                if self.path in self.auth_routes_json[self.path]:
                    self.json_page = self.auth_routes_json[self.path]
                    self.status.set_status("200 OK")
                    self.header.set_header([('Content-type', 'text/json')])
                    self.json_page = self.json_page(self.base_path, self.config).load()

                    return self.json_page

        else:
            if self.path in self.unauth_routes_html:
                self.html_page = self.unauth_routes_html[self.path]

                if self.path == "/auth":
                    """
                    Verificar o uso do try/catch aqui
                    Se já foi feito, apagar comentário
                    """
                    self.html_page = self.html_page(self.base_path, self.config, self.is_auth).load()
                    self.status.set_status("200 OK")
                    self.header.set_header([('Content-type', 'text/html')])
                else:
                    self.html_page = self.html_page(self.base_path, self.config).load()
                    self.status.set_status("200 OK")
                    self.header.set_header([('Content-type', 'text/html')])

                return self.html_page
            else:
                if self.path in self.unauth_routes_json:
                    self.json_page = self.unauth_routes_json[self.path]
                    """
                    Verificar o uso do try/catch aqui.
                    se já foi feito, apagar comentário.
                    """
                    self.json_page = self.json_page(self.base_path, self.config).load()
                    self.status.set_status("200 OK")
                    self.header.set_header([('Content-type', 'text/json')])

                    return self.json_page
