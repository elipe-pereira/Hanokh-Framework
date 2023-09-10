#!/usr/bin/env python3
# coding: utf-8

import mimetypes
from app.model.debug.log import Log
from app.model.assets.assets import Assets
from app.model.downloadables.public_download import PublicDownload
from app.model.downloadables.private_download import PrivateDownload


class ReadAssets:
    def __init__(self, base_path, header, status, auth_request):
        self.base_path = base_path
        self.file_type = ""
        self.auth_request = auth_request
        self.header = header
        self.assets = Assets(self.base_path)
        self.status = status
        self.download = PublicDownload(self.base_path)
        self.private_download = PrivateDownload(self.base_path, self.header, self.status, self.auth_request)
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
            self.status.set_status("200 OK")

            return file, self.header.get_header(), self.status.get_status()

        else:
            self.header.set_header([('Content-Type', None)])
            self.status.set_status("404 Not Found")

            return file

    def read_downloadable(self, path_info):
        self.debug.log("Lendo arquivo baixável")
        file = ""
        downloadable = self.download.get_downloadable(path_info)

        if downloadable:
            file = open(downloadable, 'rb').read()
            self.file_type = mimetypes.guess_type(downloadable)
            self.header.set_header([('Content-Type', self.file_type[0])])
            self.status.set_status("200 OK")

            return file

        else:
            self.header.set_header([('Content-Type', None)])
            self.status.set_status("404 Not Found")

            return file

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
            self.status.set_status("200 OK")

            return file

        else:
            self.debug.log("Arquivo não downloadable")

            self.header.set_header([('Content-Type', None)])
            self.status.set_status("404 Not Found")

            return file
