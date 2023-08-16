#!/usr/bin/env python3
# coding: utf-8

from model.assets.assets import Assets
from model.debug.log import Log


class AssetsController(Assets):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("AssetsController")
        Assets.__init__(self)
