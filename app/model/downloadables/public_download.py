#!/usr/bin/env python3
# coding: utf-8

from app.application import Download
from app.application import Log


class PublicDownload(Download):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("PublicDownload")
        Download.__init__(self)
