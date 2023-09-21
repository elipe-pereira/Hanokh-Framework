#!/usr/bin/env python3
# coding: utf-8

from application.assets.download.download import Download


class PrivateDownload:
    def __init__(self, base_path, config, header, status, auth, auth_request):
        # self.debug = Log()
        self.base_path = base_path
        self.config = config
        self.header = header
        self.status = status
        self.download = Download(self.base_path)
        self.auth_request = auth_request
        self.username = self.auth_request.get_user_cookie_input()
        self.files_base_dir = "/system/user"

        if self.username:
            self.files_base_dir = self.files_base_dir + "/" + self.username

        self.dir_download = ""
        self.private_files_dir = ""
        self.auth = auth

    def set_private_files_dir(self, private_files_dir):
        self.private_files_dir = private_files_dir

    def create_user_home_routes_to_download(self):
        self.dir_download = self.files_base_dir + self.private_files_dir

        self.download.set_route_prefix("/" + str(self.username))
        self.download.set_files_dir(self.dir_download)

        if self.auth.is_auth():
            self.download.create_routes_to_download()

    def is_private_downloadable(self, path_info):
        self.create_user_home_routes_to_download()

        if self.download.is_downloadable(path_info):
            # self.debug.log("É uma rota privada baixável")
            return True
        else:
            return False

    def get_private_downloadable(self, path_info):
        if self.is_private_downloadable(path_info):
            # self.debug.log("Retorna o caminho do arquivo baixável")
            return self.download.get_downloadable(path_info)
        else:
            return False
