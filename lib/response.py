#!/usr/bin/python
# -*- coding:utf-8 -*-

class BaseResponse(object):
    def __init__(self):
        self.status = True
        self.error = None
        self.data = None

    @property
    def dict(self):
        return self.__dict__