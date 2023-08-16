#!/usr/bin/env python3
# coding: utf-8

from model.downloadables.download import Download
from model.debug.log import Log


class PublicDownload(Download):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("PublicDownload")
        Download.__init__(self)
