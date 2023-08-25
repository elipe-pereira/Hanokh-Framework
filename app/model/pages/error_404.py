#!/usr/bin/env python3
# coding: utf-8

from conf import proj_config as proj
from app.application import Template


class Error404(object):
    def __init__(self):
        self.page = ""
        self.css = "/css/bootstrap.min.css"
        self.hanokh_css = "/css/hanokh.css"
        self.js = "/js/bootstrap.bundle.min.js"
        self.page_title = "HANOKH"
        self.processed_data = ""
        self.domain_base_url = proj.DOMAIN_BASE_URL
        self.page_template = Template()

    def load(self):
        self.page = self.page_template.get_page_template('404')

        if not self.page:
            return self.page_template.fail_load_template()

        self.page = str(self.page).format(self.css, self.hanokh_css)

        return self.page
