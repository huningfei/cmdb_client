#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import json
import requests
from .base import BaseHandler
from ..plugins import get_server_info
from config import settings

class AgentHandler(BaseHandler):

    def cmd(self,command,hostname=None):
        import subprocess
        return subprocess.getoutput(command)

    def handler(self):
        """
        处理Agent模式下的资产采集：网卡、内存、硬盘
        :return:
        """
        # 1. 通过调用get_server_info获取所有的资产信息：网卡、内存、硬盘
        info = get_server_info(self)

        # 2. 获取本地文件中的唯一标识
        if not os.path.exists(settings.CERT_FILE_PATH):
            # 新服务器，给API之后，应该在数据库中增加数据
            info['type'] = 'create'
        else:
            with open(settings.CERT_FILE_PATH,'r',encoding='utf-8') as f:
                cert = f.read()
            if cert == info['basic']['data']['hostname']:
                # 主机名未变更,汇报给API，API做更新
                info['type'] = 'update'
            else:
                info['cert'] = cert
                info['type'] = 'host_update'
        # 3. 发送到api
        r1 = requests.post(
            url=self.asset_api,
            data=json.dumps(info).encode('utf-8'),
            headers={
                'Content-Type':'application/json'
            }
        )
        response = r1.json()

        # 4. 唯一标识更新
        if response['status']:
            with open(settings.CERT_FILE_PATH, 'w', encoding='utf-8') as f:
                f.write(response['data'])



