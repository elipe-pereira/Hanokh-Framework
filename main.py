#!/usr/bin/python3
# coding: utf-8
import os
from wsgiref.simple_server import make_server


class Main:
    def __init__(self):
        self.status = "200 OK"
        self.headers = [("Content-type", "text/html; charset=utf-8")]
        self.base_path = os.path.dirname(os.path.realpath(__file__))

    def app(self, environ, start_response):
        start_response(self.status, self.headers)
        return

    def run(self):
        with make_server("", 8000, self.app) as httpd:
            print("Rodando servidor na porta 8000")
            print("Pressione Control-C para parar")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("Desligado...")
                httpd.server_close()


if __name__ == "__main__":
    app = Main()
    app.run()
