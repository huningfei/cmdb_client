#!/usr/bin/python
# -*- coding:utf-8 -*-
import importlib

def import_string(path):
    """
    根据字符串的形式去导入路径中的对象
    :param path:  'src.engine.agent.AgentHandler'
    :return:
    """

    module_path,cls_name = path.rsplit('.',maxsplit=1)
    module = importlib.import_module(module_path)
    return getattr(module,cls_name)