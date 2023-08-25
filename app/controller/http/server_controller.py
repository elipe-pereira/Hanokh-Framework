#!/usr/bin/python3
# coding: utf-8
from app.application import Server


class ServerController:
    def __init__(self, host_ip, port, app):
        self.host_ip = host_ip
        self.port = port
        self.app = app
        self.server = Server()
        self.server.set_host_ip(self.host_ip)
        self.server.set_port(self.port)
        self.server.set_app(self.app)
        self.server.run_server()