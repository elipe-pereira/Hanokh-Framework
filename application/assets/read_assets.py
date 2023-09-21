#!/usr/bin/env python3
# coding: utf-8

import mimetypes
from application.assets import Assets
from application.assets.download.public_download import PublicDownload
from application.assets.download.private_download import PrivateDownload


class ReadAssets:
    def __init__(self, base_path, config, header, status, auth, auth_request):
        self.base_path = base_path
        self.config = config
        self.auth = auth
        self.file_type = ""
        self.auth_request = auth_request
        self.header = header
        self.assets = Assets(self.base_path, self.config)
        self.status = status
        self.download = PublicDownload(self.base_path)
        self.private_download = PrivateDownload(
            self.base_path,
            self.config,
            self.header,
            self.status,
            self.auth,
            self.auth_request
        )
        mimetypes.init()

    def read(self, path_info):
        file = ""
        item = self.assets.get_asset_item(path_info)

        if item:
            file = open(item, 'rb').read()
            self.file_type = mimetypes.guess_type(item)
            self.header.set_header([('Content-Type', self.file_type[0])])
            self.status.set_status("200 OK")

            return file

        else:
            self.header.set_header([('Content-Type', None)])
            self.status.set_status("404 Not Found")

            return file

    def read_downloadable(self, path_info):
        file = ""
        self.download.create_routes_to_download()
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
        file = ""
        private_downloadable = self.private_download.get_private_downloadable(
            path_info)

        if private_downloadable:
            file = open(private_downloadable, 'rb').read()
            self.file_type = mimetypes.guess_type(private_downloadable)

            self.header.set_header([('Content-Type', self.file_type[0])])
            self.status.set_status("200 OK")

            return file

        else:
            self.header.set_header([('Content-Type', None)])
            self.status.set_status("404 Not Found")

            return file
