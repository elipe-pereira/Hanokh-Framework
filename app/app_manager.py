#!/usr/bin/env python3
# coding: utf-8

from app.model.conf.config import Config
from app.model.debug.log import Log
from app.model.auth.auth import Auth
from app.model.http.status import Status
from app.model.http.header import Header
from app.model.http.request import Request
from app.controller.route import RouteController
from app.controller.assets.assets import AssetsController
from app.controller.assets.read_assets import ReadAssetsController
from app.controller.download.public_download import PublicDownloadController
from app.controller.download.private_download import PrivateDownloadController


class AppManager:
    def __init__(self, base_path):
        self.proj_base_path = base_path
        self.debug = Log()
        self.header = Header()
        self.status = Status()
        self.assets = AssetsController()
        self.conf = Config(self.proj_base_path)
        self.conf.read_settings()
        self.database_is_enabled = self.conf.get_database_is_enabled()

    def get_app(self, environ, start_response):
        self.debug.log_applogo()
        self.debug.log_start("application")
        assets = AssetsController()
        wsgi_input = environ['wsgi.input'].read()
        request = Request(environ, wsgi_input)

        path = environ['PATH_INFO']
        self.debug.log_variable("path", path)

        if self.database_is_enabled == "yes":
            auth = Auth(self.header, request)
            route = RouteController(environ, self.header, self.status, auth.is_auth())

            pages_auth_routes = route.get_auth_routes().keys()
            pages_unauth_routes = route.get_unauth_routes().keys()

            if path in pages_auth_routes or path in pages_unauth_routes:
                data = route.get_route(path)
                page = bytes(str(data[0]), "utf-8")
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([page])

            is_asset = assets.is_asset(path)

            if is_asset:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read(path)
                asset = data[0]
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([asset])

            files_to_download = PublicDownloadController()
            is_downloadable = files_to_download.is_downloadable(path)

            if is_downloadable:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read_downloadable(path)
                file = data[0]
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([file])

            files_pvt_to_download = PrivateDownloadController(self.header, request)
            is_pvt_downloadable = files_pvt_to_download.is_private_downloadable(path)

            if is_pvt_downloadable:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read_private_downloadable(path)
                file = data[0]
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([file])
            else:
                path = "/404"
                data = route.get_route(path)
                page = bytes(str(data[0]), "utf-8")
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([page])

        else:
            route = RouteController(environ, self.header, self.status, False)
            pages_unauth_routes = route.get_unauth_routes().keys()

            if path in pages_unauth_routes:
                data = route.get_route(path)
                page = bytes(str(data[0]), "utf-8")
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([page])

            is_asset = assets.is_asset(path)

            if is_asset:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read(path)
                asset = data[0]
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([asset])

            files_to_download = PublicDownloadController()
            is_downloadable = files_to_download.is_downloadable(path)

            if is_downloadable:
                read_asset = ReadAssetsController(self.header, request)
                data = read_asset.read_downloadable(path)
                file = data[0]
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([file])

            else:
                route = RouteController(environ, self.header, self.status, False)

                path = "/404"
                data = route.get_route(path)
                page = bytes(str(data[0]), "utf-8")
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([page])
