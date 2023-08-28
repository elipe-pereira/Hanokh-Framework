#!/usr/bin/python3
# coding: utf-8

class ServerConfig:
    def __init__(self):
        self.host_listen = "127.0.0.1"
        self.host_port = 8000

    def set_port(self, port):
        self.host_port = port

    def get_port(self):
        return self.host_port

    def set_host_ip(self, host_ip):
        self.host_listen = host_ip

    def get_host_ip(self):
        return self.host_listen
