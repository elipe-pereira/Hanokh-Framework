#!/usr/bin/env python3
# coding: utf-8

from conf import proj_config as proj
from app.application import Template


class Auth(object):
    def __init__(self, is_auth):
        self.title = "Autenticado com sucesso!!!"
        self.bootstrap_css = "/css/bootstrap.min.css"
        self.hanokh_css = "/css/hanokh.css"
        self.bootstrap_js = "/js/bootstrap.bundle.min.js"
        self.hanokh_js = "/js/bootstrap.bundle.min.js"
        self.domain_base_url = proj.DOMAIN_BASE_URL
        self.page_template = Template()
        self.is_auth = is_auth

    def load(self):
        if self.is_auth:
            self.page = self.page_template.get_page_template('auth')

            try:
                self.page = str(self.page).format(
                    self.title,
                    self.bootstrap_css,
                    self.hanokh_css,
                    self.domain_base_url,
                    self.bootstrap_js
                )
            except Exception:
                self.page = self.page_template.fail_load_template()

            return self.page
        else:
            self.page = self.page_template.get_page_template('auth_wrong')
            self.title = "Falha na autenticação"
            self.domain_base_url = self.domain_base_url + "login"

            try:
                self.page = str(self.page).format(
                    self.title,
                    self.bootstrap_css,
                    self.hanokh_css,
                    self.domain_base_url,
                    self.hanokh_js
                )
            except Exception:
                self.page = self.page_template.fail_load_template()

            return self.page
