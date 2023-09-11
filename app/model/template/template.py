#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app.model.debug.log import Log


class Template:
    def __init__(self, base_path, config):
        self.config = config
        self.base_path = base_path
        self.template_folder = "/view/templates/" + self.config.get_template_name()
        self.folder_templates = self.base_path + self.template_folder + "/"
        self.debug = Log(self.base_path, self.config)
        self.debug.log_class("Template")

    def read_file(self, file_template):
        self.debug.log("Leando arquivo de template")

        file_template = self.folder_templates + file_template + ".html"
        self.debug.log_variable("file_template", file_template)

        file = open(file_template, 'r', encoding='utf-8')
        template = ""

        for html in file.readlines():
            template = template + html

        file.close()

        self.debug.log_variable("template", template)

        return template

    def get_page_template(self, file_template):
        template = ""

        try:
            template = self.read_file(file_template)

        except Exception:
            template = False

            return template

        return template

    def fail_load_template(self):
        return """
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset='utf-8'>
                <title>Página não encontrada!</title>
            </head>
            <body>
                <h3>Página e nenhum template encontrado!!!</h3>
            </body>
        </html>
        """
