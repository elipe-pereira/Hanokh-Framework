#!/usr/bin/env python3
# coding: utf-8

import logging
from app.model.debug.text import Text


class Log:
    def __init__(self, base_path, config):
        self.config = config
        self.base_path = base_path
        self.format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        self.log_file = self.base_path + "/system" + "/log/hanokh.log"
        self.debug = self.config.get_debug()
        self.text = Text()
        self.message = ""

    def log(self, message):
        logging.basicConfig(level=logging.DEBUG,
                            format=self.format, filename=self.log_file)

        if self.debug == "yes":
            logging.debug(message)

    def log_applogo(self):
        if self.debug == "yes":
            self.message = "logo"
            self.text.set_message(self.message)
            self.log(self.text.get_message())

    def log_bar(self):
        if self.debug == "yes":
            self.message = "bar"
            self.text.set_message(self.message)
            self.log(self.text.get_message())

    def log_start(self, method_name):
        if self.debug == "yes":
            self.message = "start"
            self.text.set_message(self.message)
            self.log(self.text.get_message().format(method_name))

    def log_class(self, classname):
        if self.debug == "yes":
            self.message = "class"
            self.text.set_message(self.message)
            self.log(self.text.get_message().format(classname))

    def log_act(self, variable_name, value, type):
        if self.debug == "yes":
            self.message = type
            self.text.set_message(self.message)
            self.log(self.text.get_message().format(variable_name, str(value)))

    def log_variable(self, variable_name, value):
        if self.debug == "yes":
            self.message = "variable value"
            self.text.set_message(self.message)
            self.log(self.text.get_message().format(variable_name, str(value)))
