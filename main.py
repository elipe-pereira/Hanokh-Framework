#!/usr/bin/python3
# coding: utf-8
import os
import sys
from app.controller.http.server_controller import ServerController
from app.model.conf.config import Config


class Main:
    def __init__(self):
        self.status = "200 OK"
        self.headers = [("Content-type", "text/html; charset=utf-8")]
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.config = Config(self.base_path)
        if self.base_path not in sys.path:
            sys.path.append(self.base_path)

    def app(self, environ, start_response):
        start_response(self.status, self.headers)
        return [b'Ola mundo!!']

    def run(self):
        ServerController("127.0.0.1", 8000, self.app)


if __name__ == "__main__":
    app = Main()
    app.run()
