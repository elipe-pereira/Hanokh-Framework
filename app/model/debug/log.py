#!/usr/bin/env python3
# coding: utf-8

import logging
from conf import proj_config as proj
from app.application import Text


class Log(object):
    def __init__(self):
        self.format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        self.log_file = proj.BASEPATH + "/system" + "/log/hanokh.log"
        self.debug_is_enable = bool(proj.DEBUG)
        self.text = Text()
        self.message = ""

    def log(self, message):
        logging.basicConfig(level=logging.DEBUG,
                            format=self.format, filename=self.log_file)

        if self.debug_is_enable:
            logging.debug(message)

    def log_applogo(self):
        if self.debug_is_enable:
            self.message = "logo"
            self.text.set_message(self.message)
            self.log(self.text.get_message())

    def log_bar(self):
        if self.debug_is_enable:
            self.message = "bar"
            self.text.set_message(self.message)
            self.log(self.text.get_message())

    def log_start(self, method_name):
        if self.debug_is_enable:
            self.message = "start"
            self.text.set_message(self.message)
            self.log(self.text.get_message().format(method_name))

    def log_class(self, classname):
        if self.debug_is_enable:
            self.message = "class"
            self.text.set_message(self.message)
            self.log(self.text.get_message().format(classname))

    def log_act(self, variable_name, value, type):
        if self.debug_is_enable:
            self.message = type
            self.text.set_message(self.message)
            self.log(self.text.get_message().format(variable_name, str(value)))

    def log_variable(self, variable_name, value):
        if self.debug_is_enable:
            self.message = "variable value"
            self.text.set_message(self.message)
            self.log(self.text.get_message().format(variable_name, str(value)))
