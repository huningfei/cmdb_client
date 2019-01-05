#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ENGINE_HANDLERS = {
    'agent':'src.engine.agent.AgentHandler',
    'ssh':'src.engine.ssh.SSHHandler',
    'salt':'src.engine.salt.SaltHandler',
}
ENGINE = 'agent'


# ########### SSH模式 ###########
# 私钥地址
SSH_PRIVATE_KEY = '/xxx/xx/xx'
SSH_PORT = 22
SSH_USER = 'cmdb'



# ############################## 插件 ################################
PLUGIN_DICT = {
    'basic':'src.plugins.basic.Basic',
    'disk':'src.plugins.disk.Disk',
    'memory':'src.plugins.memory.Memory',
    'nic':'src.plugins.network.Network',
    'cpu':'src.plugins.cpu.Cpu',
    'board':'src.plugins.main_board.MainBoard',
}

DEBUG = True

ASSET_API = "http://127.0.0.1:8000/api/asset/"


# #################### 日志路径 #################
LOG_FILE_PATH = os.path.join(BASEDIR,'log','cmdb.log')

# #################### 唯一标识路径 #################
CERT_FILE_PATH = os.path.join(BASEDIR,'config','cert')