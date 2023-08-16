#!/usr/bin/env python3
# coding: utf-8

from model.debug.log import Log
import proj_config as proj
import mimetypes
import os


class Download(object):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("Download")
        self.bpath = proj.BASEPATH
        self.route_prefix = "/files"
        self.route_files = {}
        self.routed_files = ""
        self.files_dir = "/system/public_files"
        self.file_path = ""
        self.full_path_files = self.bpath + self.files_dir
        mimetypes.init()

    def set_route_prefix(self, route_prefix):
        self.route_prefix = route_prefix
        self.debug.log_act("self.route_prefix", self.route_prefix, "set")

    def set_files_dir(self, files_dir):
        self.files_dir = files_dir
        self.debug.log_act("self.files_dir", self.files_dir, "set")

    def create_routes_to_download(self):
        self.full_path_files = self.bpath + self.files_dir
        self.debug.log_variable("self.full_path_files", self.full_path_files)

        if not os.path.isdir(self.full_path_files):
            self.debug.log("Pasta não existe")
            self.debug.log("Criando pasta")
            os.mkdir(self.full_path_files)

        files = os.listdir(self.full_path_files)

        for file in files:
            if file == ".":
                continue
            elif file == "readme.md":
                continue
            else:
                self.routed_file = self.route_prefix + "/" + file
                self.debug.log_variable("self.routed_file", self.routed_file)

                self.file_path = self.full_path_files + "/" + file
                self.debug.log_variable("self.file_path", self.file_path)

                self.route_files[self.routed_file] = self.file_path
                self.debug.log("Rota: {0} criada".format(self.routed_file))

    def is_downloadable(self, path_info):
        self.create_routes_to_download()

        if path_info in self.route_files.keys():
            self.debug.log("Rota de arquivo baixável existe")
            return True
        else:
            self.debug.log("Rota baixável não existe")
            return False

    def get_downloadable(self, path_info):
        if self.is_downloadable(path_info):
            self.debug.log("É um arquivo baixável")
            return self.route_files[path_info]
        else:
            self.debug.log("Não é baixável ou")
            self.debug.log("não foi encontrado")
            return False
