#!/usr/bin/env python3
# coding: utf-8

from model.downloadables.download import Download
from model.auth.auth import Auth
from model.debug.log import Log


class PrivateDownload(object):
    def __init__(self, header, request):
        self.debug = Log()
        self.header = header
        self.download = Download()
        self.request = request
        self.username = self.request.get_user_cookie_input()
        self.files_base_dir = "/system/user"

        if self.username:
            self.files_base_dir = self.files_base_dir + "/" + self.username

        self.dir_download = ""
        self.private_files_dir = ""
        self.auth = Auth(self.header, self.request)
        self.debug.log_class("PrivateDownload")

    def set_private_files_dir(self, private_files_dir):
        self.private_files_dir = private_files_dir
        self.debug.log_act("self.private_files_dir",
                           self.private_files_dir, "set")

    def create_user_home_routes_to_download(self):
        self.dir_download = self.files_base_dir + self.private_files_dir
        self.debug.log_variable("self.dir_download", self.dir_download)

        self.download.set_route_prefix("/" + str(self.username))
        self.download.set_files_dir(self.dir_download)

        if self.auth.is_auth():
            self.debug.log("Autenticado - Criando rotas para download")
            self.download.create_routes_to_download()

    def is_private_downloadable(self, path_info):
        self.create_user_home_routes_to_download()

        if self.download.is_downloadable(path_info):
            self.debug.log("É uma rota privada baixável")
            return True
        else:
            return False

    def get_private_downloadable(self, path_info):
        if self.is_private_downloadable(path_info):
            self.debug.log("Retorna o caminho do arquivo baixável")
            return self.download.get_downloadable(path_info)
        else:
            return False
