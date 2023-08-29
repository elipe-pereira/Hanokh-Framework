#!/usr/bin/env python3
# coding: utf-8

from app.app_manager import Log
from app.app_manager import PrivateDownload


class PrivateDownloadController(PrivateDownload):
    def __init__(self, header, request):
        self.debug = Log()
        self.debug.log_class("PrivateDownloadController")
        PrivateDownload.__init__(self, header, request)
