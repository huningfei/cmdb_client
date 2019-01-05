#!/usr/bin/python
# -*- coding:utf-8 -*-
from config import settings

class BasePlugin(object):

    def __init__(self):
        self.debug = settings.DEBUG
        self.base_dir = settings.BASEDIR

    def get_os(self,handler,host):
        # return handler.cmd('查看系统的命令',host)
        return 'linux'

    def process(self,handler,hostname):
        os = self.get_os(handler,hostname)
        if os == 'windows':
            return self.win(handler,hostname)
        else:
            return self.linux(handler,hostname)

    def win(self,handler,hostname):
        raise NotImplementedError('win must be implemented ')

    def linux(self, handler, hostname):
        raise NotImplementedError('linux must be implemented ')