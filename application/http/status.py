#!/usr/bin/python3
# coding: utf-8

class Status(object):
    def __init__(self):
        self.status = "200 OK"

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status
