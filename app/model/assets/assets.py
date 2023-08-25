#!/usr/bin/env python3
# coding: utf-8

from app.application import Log
from conf import proj_config as proj


class Assets(object):
    def __init__(self):
        self.debug = Log()
        self.debug.log_class("Assets")
        self.bpath = proj.BASEPATH
        self.favico = "/view/assets/images/favicon.ico"
        self.btstrap = "/view/assets/css/bootstrap5/bootstrap.min.css"
        self.btstrap_js = "/view/assets/js/bootstrap5/bootstrap.bundle.min.js"
        self.hnk_css = "/view/assets/css/hanokh/hanokh.css"
        self.map_assets = {
            "/favicon.ico": self.bpath + self.favico,
            "/css/bootstrap.min.css": self.bpath + self.btstrap,
            "/js/bootstrap.bundle.min.js": self.bpath + self.btstrap_js,
            "/css/hanokh.css": self.bpath + self.hnk_css
        }

    def get_map_assets(self):
        self.debug.log_act("self.map_assets", self.map_assets, "get")
        return self.map_assets

    def is_asset(self, route_asset):
        if route_asset in self.map_assets.keys():
            self.debug.log("Asset encontrado na lista de rotas")
            return True
        else:
            self.debug.log("Asset não encontrado na lista de rotas")
            return False

    def get_asset_item(self, route_asset):
        if self.is_asset(route_asset):
            self.debug.log_act(
                "self.map_assets[route_asset]", self.map_assets[route_asset],
                "get")
            return self.map_assets[route_asset]
        else:
            return False
