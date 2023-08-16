#!/usr/bin/env python3
# coding: utf-8

import mimetypes
from model.assets.assets import Assets
from model.http.status import Status
from model.downloadables.public_download import PublicDownload
from model.downloadables.private_download import PrivateDownload
from model.debug.log import Log


class ReadAssets(object):
    def __init__(self, header, request):
        self.file_type = ""
        self.request = request
        self.header = header
        self.assets = Assets()
        self.status = Status()
        self.download = PublicDownload()
        self.private_download = PrivateDownload(self.header, self.request)
        self.debug = Log()
        self.debug.log_class("ReadAssets")
        mimetypes.init()

    def read(self, path_info):
        self.debug.log("Lendo arquivo de asset")
        file = ""
        item = self.assets.get_asset_item(path_info)

        if item:
            file = open(item, 'rb').read()
            self.file_type = mimetypes.guess_type(item)
            self.header.set_header([('Content-Type', self.file_type[0])])

            return file, self.header.get_header(), self.status.get_status()

        else:
            self.header.set_header([('Content-Type', None)])
            self.status.set_status("404 Not Found")

            return file, self.header.get_header(), self.status.get_status()

    def read_downloadable(self, path_info):
        self.debug.log("Lendo arquivo baixável")
        file = ""
        downloadable = self.download.get_downloadable(path_info)

        if downloadable:
            file = open(downloadable, 'rb').read()
            self.file_type = mimetypes.guess_type(downloadable)
            self.header.set_header([('Content-Type', self.file_type[0])])

            return file, self.header.get_header(), self.status.get_status()

        else:
            self.header.set_header([('Content-Type', None)])
            self.status.set_status("404 Not Found")

            return file, self.header.get_header(), self.status.get_status()

    def read_private_downloadable(self, path_info):
        self.debug.log("Acessando método read_private_downloadable() ")
        file = ""
        private_downloadable = self.private_download.get_private_downloadable(
            path_info)

        self.debug.log_variable("private_downloadable", private_downloadable)

        if private_downloadable:
            self.debug.log("Acessando arquivo private_downloadable")

            file = open(private_downloadable, 'rb').read()
            self.file_type = mimetypes.guess_type(private_downloadable)

            self.header.set_header([('Content-Type', self.file_type[0])])

            return file, self.header.get_header(), self.status.get_status()

        else:
            self.debug.log("Arquivo não downloadable")

            self.header.set_header([('Content-Type', None)])
            self.status.set_status("404 Not Found")

            return file, self.header.get_header(), self.status.get_status()
