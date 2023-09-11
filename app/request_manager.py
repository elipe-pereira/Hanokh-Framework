#!/usr/bin/env python3
# coding: utf-8

from app.model.route import Route
from app.model.auth.auth import Auth
from app.model.assets.assets import Assets
from app.model.assets.read_assets import ReadAssets
from app.model.auth.auth_request import AuthRequest
from app.model.downloadables.public_download import PublicDownload
from app.model.downloadables.private_download import PrivateDownload


class RequestManager:
    def __init__(self):
        self.auth = None
        self.conf = None
        self.path = None
        self.route = None
        self.header = None
        self.assets = None
        self.status = None
        self.environ = None
        self.base_path = None
        self.wsgi_input = None
        self.auth_request = None
        self.pages_auth_routes = None
        self.pages_unauth_routes = None
        self.database_is_enabled = None
        self.pages_auth_routes_json = None
        self.pages_unauth_routes_json = None
        # self.debug = Log()

    def set_request_status(self, status):
        self.status = status

    def set_request_header(self, header):
        self.header = header

    def set_request_input(self, wsgi_input):
        self.wsgi_input = wsgi_input

    def set_request_environ(self, environ):
        self.environ = environ

    def set_request_basepath(self, base_path):
        self.base_path = base_path

    def set_request_conf(self, conf):
        self.conf = conf

    def get_response(self):
        self.conf.set_base_path(self.base_path)
        self.conf.read_settings()
        self.database_is_enabled = self.conf.get_database_is_enabled()
        self.auth_request = AuthRequest(self.environ, self.wsgi_input)
        self.auth = Auth(self.header, self.auth_request)
        self.route = Route(self.base_path, self.header, self.status, self.auth.is_auth())
        self.pages_auth_routes = self.route.get_auth_routes_html().keys()
        self.pages_unauth_routes = self.route.get_unauth_routes_html().keys()
        self.pages_auth_routes_json = self.route.get_auth_routes_json().keys()
        self.pages_unauth_routes_json = self.route.get_unauth_routes_json().keys()
        self.assets = Assets(self.base_path)
        # self.debug.log_applogo()
        # self.debug.log_start("application")
        # self.debug.log_variable("path", self.path)

        if self.database_is_enabled == "yes":
            if (
                    self.path in self.pages_auth_routes
                    or self.path in self.pages_unauth_routes
                    or self.path in self.pages_auth_routes_json
                    or self.path in self.pages_unauth_routes_json
            ):

                page = self.route.get_route(self.path)
                page = bytes(str(page), "utf-8")

                return iter([page])

            is_asset = self.assets.is_asset(self.path)

            if is_asset:
                read_asset = ReadAssets(self.base_path, self.header, self.status, self.auth_request)
                file = read_asset.read(self.path)
                asset = file

                return iter([asset])

            files_to_download = PublicDownload(self.base_path)
            is_downloadable = files_to_download.is_downloadable(self.path)

            if is_downloadable:
                read_asset = ReadAssets(self.base_path, self.header, self.status, self.auth_request)
                file = read_asset.read_downloadable(self.path)

                return iter([file])

            files_pvt_to_download = PrivateDownload(
                    self.base_path,
                    self.header,
                    self.status,
                    self.auth_request
                    )
            is_pvt_downloadable = files_pvt_to_download.is_private_downloadable(self.path)

            if is_pvt_downloadable:
                read_asset = ReadAssets(self.base_path, self.header, self.status, self.auth_request)
                file = read_asset.read_private_downloadable(self.path)

                return iter([file])
            else:
                self.path = "/404"
                page = self.route.get_route(self.path)
                page = bytes(str(page), "utf-8")

                return iter([page])

        else:
            self.route = Route(self.base_path, self.header, self.status, False)

            if (
                    self.path in self.pages_unauth_routes
                    or self.path in self.pages_unauth_routes_json
            ):
                page = self.route.get_route(self.path)
                page = bytes(str(page), "utf-8")

                return iter([page])

            is_asset = self.assets.is_asset(self.path)

            if is_asset:
                read_asset = ReadAssets(self.base_path, self.header, self.status, self.auth_request)
                asset = read_asset.read(self.path)

                return iter([asset])

            files_to_download = PublicDownload(self.base_path)
            is_downloadable = files_to_download.is_downloadable(self.path)

            if is_downloadable:
                read_asset = ReadAssets(self.base_path, self.header, self.status, self.auth_request)
                file = read_asset.read_downloadable(self.path)

                return iter([file])

            else:
                self.route = Route(self.base_path, self.header, self.status, False)

                self.path = "/404"
                page = self.route.get_route(self.path)
                page = bytes(str(page), "utf-8")

                return iter([page])
