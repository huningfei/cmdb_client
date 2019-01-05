#!/usr/bin/python
# -*- coding:utf-8 -*-
from config import settings
from lib.module_string import import_string

def get_server_info(handler,hostname=None):
    """
    循环所有的插件，获取所有的资产信息，然后返回
    :param handler:
    :return:
    """
    info = {}

    for name,path in settings.PLUGIN_DICT.items():
        cls = import_string(path)
        obj = cls()
        result = obj.process(handler,hostname)
        info[name] = result

    return info