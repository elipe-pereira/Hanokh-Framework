#!/usr/bin/python3
# coding: utf-8
import os
import sys
from app.app_manager import AppManager
from app.model.conf.config import Config
from app.controller.http.server_controller import ServerController


class Main:
    def __init__(self):
        self.status = "200 OK"
        self.headers = [("Content-type", "text/html; charset=utf-8")]
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.config = Config(self.base_path)
        self.app_manager = AppManager(self.base_path)
        self.server_ip = ""
        self.server_port = ""
        if self.base_path not in sys.path:
            sys.path.append(self.base_path)

    def app(self, environ, start_response):
        start_response(self.status, self.headers)
        return [b'Ola mundo']

    def run(self):
        self.config.read_settings()
        self.server_ip = self.config.get_ip_srv()
        self.server_port = self.config.get_port_srv()

        ServerController(self.server_ip, self.server_port, self.app)


if __name__ == "__main__":
    app = Main()
    app.run()
