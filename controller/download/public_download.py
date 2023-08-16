#!/usr/bin/env python3
# coding: utf-8

from model.downloadables.public_download import PublicDownload
from model.debug.log import Log


class PublicDownloadController(PublicDownload):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("PublicDownloadController")
        PublicDownload.__init__(self)
