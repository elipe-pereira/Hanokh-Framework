#!/usr/bin/env python3
# coding: utf-8

from app.model.template.template import Template


class Error404:
    def __init__(self, base_path, config):
        self.base_path = base_path
        self.config = config
        self.page = ""
        self.css = "/css/bootstrap.min.css"
        self.hanokh_css = "/css/hanokh.css"
        self.js = "/js/bootstrap.bundle.min.js"
        self.page_title = "HANOKH"
        self.processed_data = ""
        self.domain_base_url = self.config.get_base_uri()
        self.page_template = Template(self.base_path, self.config)

    def load(self):
        self.page = self.page_template.get_page_template('404')

        if not self.page:
            return self.page_template.fail_load_template()

        self.page = str(self.page).format(self.css, self.hanokh_css)

        return self.page
