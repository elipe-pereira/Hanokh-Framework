#!/usr/bin/env python3
# coding: utf-8

from app.app_manager import Route
from app.app_manager import Log


class RouteController(Route):
    def __init__(self, environ, header, status, is_auth):
        self.debug = Log()
        self.debug.log_class("RouteController")
        Route.__init__(self, environ, header, status, is_auth)
