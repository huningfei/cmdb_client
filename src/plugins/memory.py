#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import traceback
from .base import BasePlugin
from lib import convert
from lib.response import BaseResponse
from lib.log import logger

class Memory(BasePlugin):
    def win(self, handler, hostname):
        """
        获取内存信息
        :return:
        """
        result = handler.cmd('wmic memorychip', hostname)
        return result

    def linux(self,handler,hostname):
        result = BaseResponse()
        try:
            if self.debug:
                output = open(os.path.join(self.base_dir, 'files/memory.out'), 'r').read()
            else:
                shell_command = "sudo dmidecode  -q -t 17 2>/dev/null"
                output = handler.cmd(shell_command,hostname)
            result.data = self.parse(output)
        except Exception as e:
            msg = traceback.format_exc()
            result.status = False
            result.error = msg
            logger.error(msg)
        return result.dict
    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        ram_dict = {}
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufacturer',
            'Serial Number': 'sn',

        }
        devices = content.split('Memory Device')
        for item in devices:
            item = item.strip()
            if not item:
                continue
            if item.startswith('#'):
                continue
            segment = {}
            lines = item.split('\n\t')
            for line in lines:
                if len(line.split(':')) > 1:
                    key, value = line.split(':')
                else:
                    key = line.split(':')[0]
                    value = ""
                if key in key_map:
                    if key == 'Size':
                        segment[key_map['Size']] = convert.convert_mb_to_gb(value, 0)
                    else:
                        segment[key_map[key.strip()]] = value.strip()
            ram_dict[segment['slot']] = segment

        return ram_dict

