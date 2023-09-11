#!/usr/bin/python3
# coding: utf-8
import os
import sys
from app.model.conf.config import Config
from app.model.http.status import Status
from app.model.http.header import Header
from app.model.http.server import Server
from app.request_manager import RequestManager


class Main:
    def __init__(self):
        self.environ = None
        self.server_ip = None
        self.wsgi_input = None
        self.server_port = None
        self.start_response = None
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.server = Server()
        self.status = Status()
        self.header = Header()
        self.config = Config()
        self.request_manager = RequestManager()
        if self.base_path not in sys.path:
            sys.path.append(self.base_path)

    def app(self, environ, start_response):
        self.environ = environ
        self.wsgi_input = self.environ['wsgi.input']
        self.request_manager.set_request_environ(self.environ)
        self.request_manager.set_request_status(self.status)
        self.request_manager.set_request_header(self.header)
        self.request_manager.set_request_input(self.wsgi_input)
        self.request_manager.set_request_basepath(self.base_path)
        self.request_manager.set_request_conf(self.config)

        self.start_response = start_response
        self.start_response(self.status.get_status(), self.header.get_header())

        return self.request_manager.get_response()

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
    app = Main()
    app.run()
