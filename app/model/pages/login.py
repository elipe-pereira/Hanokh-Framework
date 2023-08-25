#!/usr/bin/env python3
# coding: utf-8

from conf import proj_config as proj
from app.application import Template


class Login(object):
    def __init__(self):
        self.title = "Faça o Login"
        self.bootstrap_css = "/css/bootstrap.min.css"
        self.hanokh_css = "/css/hanokh.css"
        self.bootstrap_js = "/js/bootstrap.bundle.min.js"
        self.hanokh_js = ""
        self.domain_base_url = proj.DOMAIN_BASE_URL
        self.page_template = Template()

    def load(self):
        self.page = self.page_template.get_page_template('login')

        if not self.page:
            self.page = self.page_template.get_page_template('404')
            self.page = str(self.page).format(self.css, self.hanokh_css)

            return self.page

        self.page_title = "Login"

        self.page = str(self.page).format(
            self.title,
            self.bootstrap_css,
            self.hanokh_css
        )

        return self.page
