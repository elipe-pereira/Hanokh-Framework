#!/usr/bin/python3
# coding: utf-8

from app.application import Log


class Status(object):
    def __init__(self):
        self.status = "200 OK"
        self.debug = Log()
        self.debug.log_class("Status")

    def set_status(self, status):
        self.status = status
        self.debug.log_act("self.status", self.status, "set")

    def get_status(self):
        self.debug.log_act("self.status", self.status, "get")
        return self.status
