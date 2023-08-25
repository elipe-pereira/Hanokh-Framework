#!/usr/bin/env python3
# coding: utf-8

from app.application import Route
from app.application import Log


class RouteController(Route):
    def __init__(self, environ, header, status, is_auth):
        self.debug = Log()
        self.debug.log_class("RouteController")
        Route.__init__(self, environ, header, status, is_auth)
