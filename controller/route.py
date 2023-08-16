#!/usr/bin/env python3
# coding: utf-8

from model.route import Route
from model.debug.log import Log


class RouteController(Route):
    def __init__(self, environ, header, status, is_auth):
        self.debug = Log()
        self.debug.log_class("RouteController")
        Route.__init__(self, environ, header, status, is_auth)
