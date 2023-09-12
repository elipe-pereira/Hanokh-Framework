#!/usr/bin/env python3
# coding: utf-8

# from app.model.debug.log import Log
import os
import mimetypes


class Download:
    def __init__(self, base_path):
        self.base_path = base_path
        self.route_prefix = "/samples"
        self.route_files = {}
        self.routed_file = ""
        self.files_dir = "/system/public_files"
        self.file_path = ""
        self.full_path_files = self.base_path + self.files_dir
        mimetypes.init()

    def set_route_prefix(self, route_prefix):
        self.route_prefix = route_prefix

    def set_files_dir(self, files_dir):
        self.files_dir = files_dir

    def create_routes_to_download(self):
        self.full_path_files = self.base_path + self.files_dir

        if not os.path.isdir(self.full_path_files):
            os.mkdir(self.full_path_files)

        files = os.listdir(self.full_path_files)

        for file in files:
            if file == ".":
                continue
            elif file == "readme.md":
                continue
            else:
                self.routed_file = self.route_prefix + "/" + file

                self.file_path = self.full_path_files + "/" + file

                self.route_files[self.routed_file] = self.file_path

    def is_downloadable(self, path_info):
        self.create_routes_to_download()

        if path_info in self.route_files.keys():
            return True
        else:
            return False

    def get_downloadable(self, path_info):
        if self.is_downloadable(path_info):
            return self.route_files[path_info]
        else:
            return False
