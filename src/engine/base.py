#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import requests
from config import settings
from ..plugins import get_server_info

class BaseHandler(object):

    def __init__(self):
        self.asset_api = settings.ASSET_API

    def cmd(self,command, hostname=None):
        raise NotImplementedError('cmd must be implemented')

    def handler(self):
        """
        约束所有的派生类都必须实现handler方法
        :return:
        """
        raise NotImplementedError('handler must be implemented')

class SaltAndSSHHandler(BaseHandler):
    def handler(self):
        """
        处理SSH模式下的资产采集
        :return:
        """
        from concurrent.futures import ThreadPoolExecutor
        # 1. 获取未采集的主机的列表
        r1 = requests.get(url=self.asset_api)
        hostname_list = r1.json()
        pool = ThreadPoolExecutor(20)
        for hostname in hostname_list:
            pool.submit(self.task, hostname)

    def task(self, hostname):
        info = get_server_info(self, hostname)
        # 2. 发送到api
        r1 = requests.post(
                url=self.asset_api,
                data=json.dumps(info).encode('utf-8'),
                headers={
                    'Content-Type': 'application/json'
                }
        )
        print(r1)
