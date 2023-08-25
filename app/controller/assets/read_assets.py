#!/usr/bin/env python3
# coding: utf-8

from app.application import ReadAssets
from app.application import Log


class ReadAssetsController(ReadAssets):
    def __init__(self, header, request):
        self.debug = Log()
        self.debug.log_class("ReadAssetsController")
        ReadAssets.__init__(self, header, request)
