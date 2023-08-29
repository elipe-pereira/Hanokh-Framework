#!/usr/bin/python3
# coding: utf-8

from app.app_manager import Log


class Header(object):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("Header")
        self.header = [('content-type', 'text/html')]

    def set_header(self, header):
        self.header = header
        self.debug.log_act("self.header", self.header, "set")

    def get_header(self):
        self.debug.log_act("self.header", self.header, "get")
        return self.header
