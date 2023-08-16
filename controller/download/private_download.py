#!/usr/bin/env python3
# coding: utf-8

from model.debug.log import Log
from model.downloadables.private_download import PrivateDownload


class PrivateDownloadController(PrivateDownload):
    def __init__(self, header, request):
        self.debug = Log()
        self.debug.log_class("PrivateDownloadController")
        PrivateDownload.__init__(self, header, request)
