#!/usr/bin/env python3
# coding: utf-8

class Text(object):
    def __init__(self):
        self.text_start = "Start {0}"
        self.text_setting = "Setting {0}: {1}"
        self.text_getting = "Getting {0}: {1}"
        self.text_building_class = "Building class {0}"
        self.text_vr_value = "Variável {0}: {1}"
        self.text_cleaning = "Cleaning {0}: {1}"
        self.message_maps = {
            "logo": """
##############################################################################
##############################################################################

            #     #      ##       #    #   ####    #   # #     #
            #     #     #  #      ##   #  #    #   #  #  #     #
            #######    #    #     # #  # #      #  ##    #######
            #     #   ########    #  # #  #    #   # #   #     #
            #     #  #        #   #    #   ####    #  #  #     #

    ##### ####      #     #       # #### #       #      #   ####   #####  #  #
    #     #   #    # #    ##     ## #     #     ##     #   #    #  #    # # #
    ##### ####    #   #   # #   # # ####   #   #  #   #   #      # #####  ##
    #     # #    #######  #  # #  # #       # #    # #     #    #  # #    # #
    #     #   # #       # #   #   # ####     #      #       ####   #   #  #  #

##############################################################################
##############################################################################
            """,
            "start": self.text_start,
            "class": self.text_building_class,
            "set": self.text_setting,
            "get": self.text_getting,
            "variable value": self.text_vr_value,
            "clean": self.text_cleaning
        }
        self.text_message = ""

    def set_message(self, message):
        if message in self.message_maps.keys():
            self.text_message = self.message_maps[message]

    def get_message(self):
        return self.text_message
