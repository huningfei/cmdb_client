#!/usr/bin/python
# -*- coding:utf-8 -*-
import importlib
from config import settings
from lib.module_string import import_string
def run():
    """
    采集资产的入口
    :return:
    """
    # 'src.engine.agent.AgentHandler'
    engine_path = settings.ENGINE_HANDLERS.get(settings.ENGINE)
    cls = import_string(engine_path)
    obj = cls()
    obj.handler()