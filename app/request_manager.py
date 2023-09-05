#!/usr/bin/env python3
# coding: utf-8

from app.model.route import Route
from app.model.auth.auth import Auth
from app.model.auth.request import Request
from app.model.assets.assets import Assets


class RequestManager:
    def __init__(self):
        self.proj_base_path = None
        self.wsgi_input = None
        self.environ = None
        self.path = None
        self.conf = None
        self.database_is_enabled = self.conf.get_database_is_enabled()
        # self.debug = Log()
        self.header = None
        self.status = None
        self.assets = Assets()
        self.request = Request(environ, self.wsgi_input)
        self.auth = Auth(self.header, self.request)
        self.route = Route(self.environ, self.header, self.status, self.auth.is_auth())
        self.pages_auth_routes = self.route.get_auth_routes_html().keys()
        self.pages_unauth_routes = self.route.get_unauth_routes_html()
        self.pages_auth_routes_json = self.route.get_auth_routes_json()
        self.pages_unauth_routes_json = self.route.get_unauth_routes_json()

    def set_request_status(self, status):
        self.status = status

    def set_request_header(self, header):
        self.header = header

    def set_request_input(self, wsgi_input):
        self.wsgi_input = wsgi_input

    def set_request_environ(self, environ):
        self.environ = environ

    def set_request_basepath(self, base_path):
        self.proj_base_path = base_path

    def set_request_conf(self, conf):
        self.conf = conf

    def get_response(self):
        # self.debug.log_applogo()
        # self.debug.log_start("application")
        # self.debug.log_variable("path", self.path)

        if self.database_is_enabled == "yes":
            if self.path in self.pages_auth_routes or self.path in self.pages_unauth_routes:
                data = self.route.get_route(self.path)
                page = bytes(str(data[0]), "utf-8")
                status = data[2]
                response_headers = data[1]

                return iter([page])

            is_asset = assets.is_asset(path)

            if is_asset:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read(path)
                asset = data[0]
                status = data[2]
                response_headers = data[1]

                return iter([asset])

            files_to_download = PublicDownloadController()
            is_downloadable = files_to_download.is_downloadable(path)

            if is_downloadable:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read_downloadable(path)
                file = data[0]
                status = data[2]
                response_headers = data[1]

                return iter([file])

            files_pvt_to_download = PrivateDownloadController(self.header, request)
            is_pvt_downloadable = files_pvt_to_download.is_private_downloadable(path)

            if is_pvt_downloadable:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read_private_downloadable(path)
                file = data[0]
                status = data[2]
                response_headers = data[1]

                return iter([file])
            else:
                path = "/404"
                data = route.get_route(path)
                page = bytes(str(data[0]), "utf-8")
                status = data[2]
                response_headers = data[1]

                return iter([page])

        else:
            route = RouteController(environ, self.header, self.status, False)
            pages_unauth_routes = route.get_unauth_routes().keys()

            if path in pages_unauth_routes:
                data = route.get_route(path)
                page = bytes(str(data[0]), "utf-8")
                status = data[2]
                response_headers = data[1]

                return iter([page])

            is_asset = assets.is_asset(path)

            if is_asset:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read(path)
                asset = data[0]
                status = data[2]
                response_headers = data[1]

                return iter([asset])

            files_to_download = PublicDownloadController()
            is_downloadable = files_to_download.is_downloadable(path)

            if is_downloadable:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read_downloadable(path)
                file = data[0]
                status = data[2]
                response_headers = data[1]

                return iter([file])

            else:
                route = RouteController(environ, self.header, self.status, False)

                path = "/404"
                data = route.get_route(path)
                page = bytes(str(data[0]), "utf-8")
                status = data[2]
                response_headers = data[1]

                return iter([page])
