#!/usr/bin/env python3
# coding: utf-8

from app.app_manager import Download
from app.app_manager import Log


class PublicDownload(Download):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("PublicDownload")
        Download.__init__(self)
