#!/usr/bin/env python3
# coding: utf-8

from model.assets.read_assets import ReadAssets
from model.debug.log import Log


class ReadAssetsController(ReadAssets):
    def __init__(self, header, request):
        self.debug = Log()
        self.debug.log_class("ReadAssetsController")
        ReadAssets.__init__(self, header, request)
