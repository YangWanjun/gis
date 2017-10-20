# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class CustomException(Exception):
    def __init__(self, message):
        self.message = message


class FileNotExistsException(CustomException):
    def __init__(self, path):
        message = "{}が見つかりません。".format(path)
        CustomException.__init__(self, message)
