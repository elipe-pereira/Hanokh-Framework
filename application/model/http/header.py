#!/usr/bin/python3
# coding: utf-8

class Header:
    def __init__(self):
        self.header = [('content-type', 'text/html')]

    def set_header(self, header):
        self.header = header

    def get_header(self):
        return self.header
