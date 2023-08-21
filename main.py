#!/usr/bin/python3
# coding: utf-8
import os
from controller.http.server_controller import ServerController

class Main:
    def __init__(self):
        self.status = "200 OK"
        self.headers = [("Content-type", "text/html; charset=utf-8")]
        self.base_path = os.path.dirname(os.path.realpath(__file__))

    def app(self, environ, start_response):
        start_response(self.status, self.headers)
        return [b'Ola mundo!!']

    def run(self):
        ServerController("127.0.0.1", 8000, self.app)



if __name__ == "__main__":
    app = Main()
    app.run()
