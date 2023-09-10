#!/usr/bin/env python3
# coding: utf-8

"""A Classe Route gerencia somente
as rotas relacionadas às páginas html.
Ativos (imagens, css e javascript) são
gerenciados em outra classe.
"""
# from app.model.debug.log import Log
from app.model.pages.auth import Auth
from app.model.pages.start import Start
from app.model.pages.login import Login
from app.model.http.cookie import Cookie
from app.model.pages.error_404 import Error404


class Route(object):
    def __init__(self, environ, header, status, is_auth=False):
        self.environ = environ
        self.route = self.environ['PATH_INFO']
        self.header = header
        self.status = status
        self.cookie = Cookie()
        # self.debug = Log()
        self.is_auth = is_auth
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

    def get_auth_routes_html(self):
        return self.auth_routes_html

    def get_unauth_routes_html(self):
        return self.unauth_routes_html

    """
    Rotas com o content-type do
    tipo text/json para acomodar
    o uso de apis.
    """
    def get_auth_routes_json(self):
        return self.auth_routes_json

    def get_unauth_routes_json(self):
        return self.unauth_routes_json

    """
    As rotas /auth e /login possuem um tratamento
    especial em relação às outras rotas.
    """
    def get_route(self, path):
        self.path = path
        if self.is_auth:
            # self.debug.log("Autenticado")
            if self.path in self.auth_routes_html:
                self.html_page = self.auth_routes_html[self.path]
                if self.path == "/auth":
                    self.html_page = self.html_page(self.is_auth).load()
                elif self.path == "/login":
                    self.cookie.clean_cookie_ssid()
                    self.cookie.clean_cookie_user()
                    self.status.set_status("200 OK")
                    self.header.set_header([
                        ('Content-type', 'text/html'),
                        ('set-cookie', self.cookie.get_cookie_ssid()),
                        ('set-cookie', self.cookie.get_cookie_user())

                    ])
                    self.html_page = self.html_page().load()
                else:
                    self.header.set_header([('Content-type', 'text/html')])
                    self.html_page = self.html_page().load()

                return self.html_page
            else:
                if self.path in self.auth_routes_json[self.path]:
                    self.json_page = self.auth_routes_json[self.path]
                    self.status.set_status("200 OK")
                    self.header.set_header([('Content-type', 'text/json')])
                    self.json_page = self.json_page().load()

                    return self.json_page

        else:
            # self.debug.log("Não autenticado")
            if self.path in self.unauth_routes_html:
                self.html_page = self.unauth_routes_html[self.path]

                if self.path == "/auth":
                    """
                    Verificar o uso do try/catch aqui
                    Se já foi feito, apagar comentário
                    """
                    self.html_page = self.html_page(self.is_auth).load()
                    self.status.set_status("200 OK")
                    self.header.set_header([('Content-type', 'text/html')])
                else:
                    self.html_page = self.html_page().load()
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
                    self.json_page = self.json_page().load()
                    self.status.set_status("200 OK")
                    self.header.set_header([('Content-type', 'text/json')])

                    return self.json_page
