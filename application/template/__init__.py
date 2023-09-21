#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Template:
    def __init__(self, base_path, config):
        self.config = config
        self.base_path = base_path
        self.template_folder = "/application/template/" + self.config.get_template_name()
        self.folder_templates = self.base_path + self.template_folder + "/"

    def read_file(self, file_template):
        file_template = self.folder_templates + file_template + ".html"

        file = open(file_template, 'r', encoding='utf-8')
        template = ""

        for html in file.readlines():
            template = template + html

        file.close()

        return template

    def get_page_template(self, file_template):
        template = ""

        try:
            template = self.read_file(file_template)

        except:
            template = False
            return template

        return template

    @staticmethod
    def fail_load_template():
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
