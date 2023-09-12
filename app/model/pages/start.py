#!/usr/bin/env python3
# coding: utf-8

from app.model.template.template import Template


class Start:
    def __init__(self, base_path, config):
        self.base_path = base_path
        self.config = config
        # self.page_title = "Página inicial"
        self.page = ""
        # self.bootstrap_css = "/css/bootstrap.min.css"
        # self.hanokh_css = "/css/hanokh.css"
        # self.bootstrap_js = "/js/bootstrap.bundle.min.js"
        # self.hanokh_js = ""
        self.domain_base_url = self.config.get_base_uri()
        self.page_template = Template(self.base_path, self.config)

    @staticmethod
    def load():
        # self.page = self.page_template.get_page_template('start')

        # if not self.page:
        #     self.page = self.page_template.fail_load_template()
        #     return self.page

        # self.page = str(self.page).format(
        #     self.page_title,
        #     self.bootstrap_css,
        #     self.hanokh_css
        # )

        # return self.page
        return """
            <html>
                <head>
                    <title>Pagina de teste</title>
                    <link rel="icon" type="image/vnd.microsoft.icon" href="/favicon.ico"/>
                </head>
                <body>
                    <h1>Hanokh Framework</h1>
                    <hr>
                </body>
            </html>
        """
