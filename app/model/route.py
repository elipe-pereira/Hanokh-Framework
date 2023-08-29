#!/usr/bin/env python3
# coding: utf-8

from app.app_manager import Log
from app.app_manager import Cookie
from app.app_manager import Start
from app.app_manager import Login
from app.app_manager import Auth
from app.app_manager import Error404


class Route(object):
    def __init__(self, environ, header, status, is_auth=False):
        self.environ = environ
        self.route = self.environ['PATH_INFO']
        self.header = header
        self.status = status
        self.cookie = Cookie()
        self.debug = Log()
        self.is_auth = is_auth
        self.auth_routes = {
            '/': Start,
            '/login': Login,
            '/auth': Auth,
            '/404': Error404
        }
        self.unauth_routes = {
            '/': Start,
            '/auth': Auth,
            '/login': Login,
            '/404': Error404,
            '/start': Start
        }

    def get_auth_routes(self):
        return self.auth_routes

    def get_unauth_routes(self):
        return self.unauth_routes

    def get_route(self, path):
        if self.is_auth:
            self.debug.log("Autenticado")
            page = self.auth_routes[path]
            html = ""

            if path == "/auth":
                html = page(self.is_auth).load()
            elif path == "/login":
                self.cookie.clean_cookie_ssid()
                self.cookie.clean_cookie_user()
                self.header.set_header([
                    ('Content-type', 'text/html'),
                    ('set-cookie', self.cookie.get_cookie_ssid()),
                    ('set-cookie', self.cookie.get_cookie_user())

                ])

                html = page().load()
            else:
                html = page().load()

            self.page_header = self.header.get_header()
            self.page_status = self.status.get_status()

            return html, self.page_header, self.page_status

        else:
            self.debug.log("Não autenticado")

            page = self.unauth_routes[path]
            html = ""

            if path == "/auth":
                html = page(self.is_auth).load()
            else:
                html = page().load()

            self.page_header = self.header.get_header()
            self.page_status = self.status.get_status()

            return html, self.page_header, self.page_status
