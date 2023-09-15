#!/usr/bin/env python3
# coding: utf-8

from application.model.template.template import Template


class Login(object):
    def __init__(self, base_path, config):
        self.base_path = base_path
        self.config = config
        self.page_title = "Login"
        self.page = ""
        self.title = "Faça o Login"
        self.bootstrap_css = "/css/bootstrap.min.css"
        self.hanokh_css = "/css/hanokh.css"
        self.bootstrap_js = "/js/bootstrap.bundle.min.js"
        self.hanokh_js = ""
        self.domain_base_url = self.config.get_base_uri()
        self.page_template = Template(self.base_path, self.config)

    def load(self):
        self.page = self.page_template.get_page_template('login')

        if not self.page:
            self.page = self.page_template.get_page_template('404')
            self.page = str(self.page).format(self.bootstrap_css, self.hanokh_css)

            return self.page

        self.page_title = "Login"

        self.page = str(self.page).format(
            self.title,
            self.bootstrap_css,
            self.hanokh_css
        )

        return self.page
