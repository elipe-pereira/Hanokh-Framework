#!/usr/bin/env python3
# coding: utf-8

from app.app_manager import ReadAssets
from app.app_manager import Log


class ReadAssetsController(ReadAssets):
    def __init__(self, header, request):
        self.debug = Log()
        self.debug.log_class("ReadAssetsController")
        ReadAssets.__init__(self, header, request)
