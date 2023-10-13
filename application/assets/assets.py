#!/usr/bin/env python3
# coding: utf-8

class Assets(object):
    def __init__(self, basepath, config):
        self.basepath = basepath
        self.config = config
        self.favico = "/application/assets/images/favicon.ico"
        self.btstrap = "/application/assets/css/bootstrap5/bootstrap.min.css"
        self.btstrap_js = "/application/assets/js/bootstrap5/bootstrap.bundle.min.js"
        self.hnk_css = "/application/assets/css/hanokh/hanokh.css"
        self.map_assets = {
            "/favicon.ico": self.basepath + self.favico,
            "/css/bootstrap.min.css": self.basepath + self.btstrap,
            "/js/bootstrap.bundle.min.js": self.basepath + self.btstrap_js,
            "/css/hanokh.css": self.basepath + self.hnk_css
        }

    def get_map_assets(self):
        return self.map_assets

    def is_asset(self, route_asset):
        if route_asset in self.map_assets.keys():
            return True
        else:
            return False

    def get_asset_item(self, route_asset):
        if self.is_asset(route_asset):
            print(self.map_assets[route_asset])
            return self.map_assets[route_asset]
        else:
            return False
