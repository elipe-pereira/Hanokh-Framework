#!/usr/bin/python3
# coding: utf-8

from application.auth.auth import Auth
from application.route.route import Route
from application.assets.assets import Assets
from application.auth.auth_request import AuthRequest
from application.assets.read_assets import ReadAssets
from application.assets.download.public_download import PublicDownload
from application.assets.download.private_download import PrivateDownload


class Request:
    def __init__(self):
        self.auth = None
        self.conf = None
        self.path = None
        self.page = None
        self.route = None
        self.header = None
        self.assets = None
        self.status = None
        self.environ = None
        self.basepath = None
        self.db_enabled = None
        self.wsgi_input = None
        self.auth_request = None
        # html routes
        self.auth_routes = None
        self.unauth_routes = None
        # json routes
        self.auth_routes_jsn = None
        self.unauth_routes_jsn = None

    def set_status(self, status):
        self.status = status

    def set_header(self, header):
        self.header = header

    def set_input(self, wsgi_input):
        self.wsgi_input = wsgi_input

    def set_environ(self, environ):
        self.environ = environ

    def set_basepath(self, basepath):
        self.basepath = basepath

    def set_conf(self, conf):
        self.conf = conf
        self.conf.set_base_path(self.basepath)
        self.conf.read_settings()

    def set(self, path_info):
        self.path = path_info
        self.db_enabled = self.conf.get_database_is_enabled()

        self.auth_request = AuthRequest(
            self.environ,
            self.wsgi_input
        )
        self.auth = Auth(
            self.basepath,
            self.conf,
            self.header,
            self.status,
            self.auth_request
        )
        self.route = Route(
            self.basepath,
            self.header,
            self.status,
            self.auth.is_auth()
        )
        self.route = Route(
            self.basepath,
            self.header,
            self.status,
            False
        )
        self.auth_routes = self.route.get_auth_routes_html().keys()
        self.unauth_routes = self.route.get_unauth_routes_html().keys()
        self.auth_routes_jsn = self.route.get_auth_routes_json().keys()
        self.unauth_routes_jsn = self.route.get_unauth_routes_json().keys()

        self.assets = Assets(
            self.basepath,
            self.conf
        )

        if self.db_enabled == "yes":
            if (
                    self.path in self.auth_routes
                    or self.path in self.unauth_routes
                    or self.path in self.auth_routes_jsn
                    or self.path in self.unauth_routes_jsn
            ):

                self.page = self.route.get_route(self.path)
                self.page = bytes(str(self.page), "utf-8")
                return iter([self.page])

            is_asset = self.assets.is_asset(self.path)
            if is_asset:
                read_asset = ReadAssets(
                    self.basepath,
                    self.conf,
                    self.header,
                    self.status,
                    self.auth,
                    self.auth_request
                )
                file = read_asset.read(self.path)
                self.page = file
                return iter([self.page])

            files_to_download = PublicDownload(self.basepath)
            is_downloadable = files_to_download.is_downloadable(self.path)
            if is_downloadable:
                read_asset = ReadAssets(
                    self.basepath,
                    self.conf,
                    self.header,
                    self.status,
                    self.auth,
                    self.auth_request
                )
                file = read_asset.read_downloadable(self.path)
                self.page = file
                return iter([self.page])

            files_pvt_to_download = PrivateDownload(
                    self.basepath,
                    self.conf,
                    self.header,
                    self.status,
                    self.auth,
                    self.auth_request
                    )
            is_pvt_downloadable = files_pvt_to_download.is_private_downloadable(self.path)
            if is_pvt_downloadable:
                read_asset = ReadAssets(
                    self.basepath,
                    self.conf,
                    self.header,
                    self.status,
                    self.auth,
                    self.auth_request
                )
                file = read_asset.read_private_downloadable(self.path)
                self.page = file
                return iter([self.page])
            else:
                self.path = "/404"
                self.page = self.route.get_route(self.path)
                self.page = bytes(str(self.page), "utf-8")
                return iter([self.page])
        else:
            self.route = Route(
                self.basepath,
                self.header,
                self.status,
                False
            )
            if (
                    self.path in self.unauth_routes
                    or self.path in self.unauth_routes_jsn
            ):
                self.page = self.route.get_route(self.path)
                self.page = bytes(str(self.page), "utf-8")
                return iter([self.page])

            is_asset = self.assets.is_asset(self.path)
            if is_asset:
                read_asset = ReadAssets(
                    self.basepath,
                    self.conf,
                    self.header,
                    self.status,
                    self.auth,
                    self.auth_request
                )
                asset = read_asset.read(self.path)
                self.page = asset
                return iter([self.page])

            files_to_download = PublicDownload(self.basepath)
            is_downloadable = files_to_download.is_downloadable(self.path)
            if is_downloadable:
                read_asset = ReadAssets(
                    self.basepath,
                    self.conf,
                    self.header,
                    self.status,
                    self.auth,
                    self.auth_request
                )
                file = read_asset.read_downloadable(self.path)
                self.page = file
                return iter([self.page])
            else:
                self.route = Route(
                    self.basepath,
                    self.header,
                    self.status,
                    False
                )
                self.path = "/404"
                self.page = self.route.get_route(self.path)
                self.page = bytes(str(self.page), "utf-8")
                return iter([self.page])

    def get(self):
        return iter([self.page])
