#!/usr/bin/python3
# coding: utf-8
import os
import sys

from application.request import Request
from application.model.conf.config import Config
from application.model.http.status import Status
from application.model.http.header import Header
from application.model.http.server import Server


class App:
    def __init__(self):
        self.page = None
        self.environ = None
        self.server_ip = None
        self.path_info = None
        self.wsgi_input = None
        self.server_port = None
        self.start_response = None
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.server = Server()
        self.status = Status()
        self.header = Header()
        self.config = Config()
        self.request = Request()
        if self.base_path not in sys.path:
            sys.path.append(self.base_path)

    def app(self, environ, start_response):
        self.environ = environ
        self.wsgi_input = self.environ['wsgi.input']
        self.path_info = self.environ['PATH_INFO']
        self.request.set_request_environ(self.environ)
        self.request.set_request_status(self.status)
        self.request.set_request_header(self.header)
        self.request.set_request_input(self.wsgi_input)
        self.request.set_request_basepath(self.base_path)
        self.request.set_request_conf(self.config)

        self.page = self.request.get_response(self.path_info)

        start_response(self.status.get_status(), self.header.get_header())

        return self.page

    def run(self):
        self.config.set_base_path(self.base_path)
        self.config.read_settings()
        self.server_ip = self.config.get_ip_srv()
        self.server_port = self.config.get_port_srv()
        self.server.set_host_ip(self.server_ip)
        self.server.set_port(self.server_port)
        self.server.set_app(self.app)

        self.server.run_server()


if __name__ == "__main__":
    app = App()
    app.run()
