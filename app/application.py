#!/usr/bin/env python3
# coding: utf-8

from model.debug.log import Log
from model.auth.auth import Auth
from model.http.status import Status
from model.http.header import Header
from model.http.request import Request
from controller.route import RouteController
from controller.assets.assets import AssetsController
from controller.assets.read_assets import ReadAssetsController
from controller.download.public_download import PublicDownloadController
from controller.download.private_download import PrivateDownloadController


class Application:
    def __int__(self):
        self.debug = Log()
        self.header = Header()
        self.status = Status()
        self.assets = AssetsController()
        self.database_is_enabled = ""

    def get_app(self, environ, start_response):
        debug = Log()
        debug.log_applogo()
        debug.log_start("application")
        header = Header()
        status = Status()
        assets = AssetsController()
        database_is_enabled = proj.DATABASE_ENABLED
        wsgi_input = environ['wsgi.input'].read()
        request = Request(environ, wsgi_input)

        path = environ['PATH_INFO']
        debug.log_variable("path", path)

        if database_is_enabled == "yes":
            auth = Auth(header, request)
            route = RouteController(environ, header, status, auth.is_auth())

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
                read_asset = ReadAssetsController(header, request)
                data = read_asset.read(path)
                asset = data[0]
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([asset])

            files_to_download = PublicDownloadController()
            is_downloadable = files_to_download.is_downloadable(path)

            if is_downloadable:
                read_asset = ReadAssetsController(header, request)
                data = read_asset.read_downloadable(path)
                file = data[0]
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([file])

            files_pvt_to_download = PrivateDownloadController(header, request)
            is_pvt_downloadable = files_pvt_to_download.is_private_downloadable(path)

            if is_pvt_downloadable:
                read_asset = ReadAssetsController(header, request)
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
            route = RouteController(environ, header, status, False)
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
                read_asset = ReadAssetsController(header, request)
                data = read_asset.read(path)
                asset = data[0]
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([asset])

            files_to_download = PublicDownloadController()
            is_downloadable = files_to_download.is_downloadable(path)

            if is_downloadable:
                read_asset = ReadAssetsController(header, request)
                data = read_asset.read_downloadable(path)
                file = data[0]
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([file])

            else:
                route = RouteController(environ, header, status, False)

                path = "/404"
                data = route.get_route(path)
                page = bytes(str(data[0]), "utf-8")
                status = data[2]
                response_headers = data[1]

                start_response(status, response_headers)

                return iter([page])
