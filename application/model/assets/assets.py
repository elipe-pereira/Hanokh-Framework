#!/usr/bin/env python3
# coding: utf-8

class Assets(object):
    def __init__(self, base_path, config):
        self.base_path = base_path
        self.config = config
        self.favico = "/application/view/assets/images/favicon.ico"
        self.btstrap = "/application/view/assets/css/bootstrap5/bootstrap.min.css"
        self.btstrap_js = "/application/view/assets/js/bootstrap5/bootstrap.bundle.min.js"
        self.hnk_css = "/application/view/assets/css/hanokh/hanokh.css"
        self.map_assets = {
            "/favicon.ico": self.base_path + self.favico,
            "/css/bootstrap.min.css": self.base_path + self.btstrap,
            "/js/bootstrap.bundle.min.js": self.base_path + self.btstrap_js,
            "/css/hanokh.css": self.base_path + self.hnk_css
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
