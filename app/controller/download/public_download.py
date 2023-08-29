#!/usr/bin/env python3
# coding: utf-8

from app.app_manager import PublicDownload
from app.app_manager import Log


class PublicDownloadController(PublicDownload):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("PublicDownloadController")
        PublicDownload.__init__(self)
