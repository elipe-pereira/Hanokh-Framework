#!/usr/bin/env python3
# coding: utf-8

from application.model.assets.downloadables.download import Download
# from application.model.debug.log import Log


class PublicDownload(Download):
    def __init__(self, base_path):
        self.base_path = base_path
        # self.debug = Log()
        # self.debug.log_class("PublicDownload")
        Download.__init__(self, self.base_path)
