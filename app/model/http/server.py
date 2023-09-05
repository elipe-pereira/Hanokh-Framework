#!/usr/bin/python3
# coding: utf-8
from wsgiref.simple_server import make_server


class Server:
    def __init__(self):
        self.port = 8000
        self.host_ip = "127.0.0.1"
        self.app = None

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return self.port

    def set_host_ip(self, host_ip):
        self.host_ip = host_ip

    def get_host_ip(self):
        return self.host_ip

    def set_app(self, app):
        self.app = app

    def get_app(self):
        return self.app

    def run_server(self):
        with make_server(self.host_ip, self.port, self.app) as httpd:
            print("Rodando servidor em {0} e porta {1}".
                  format(self.host_ip, self.port))
            print("Pressione Control-C para parar")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("Desligado...")
                httpd.server_close()
