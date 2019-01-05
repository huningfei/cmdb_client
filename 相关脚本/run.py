#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json

def agent():
    """
    获取当前服务器的资产信息并提交给api
    :return:
    """
    # 1. 获取资产信息：硬盘、网卡、内存...(linux或win的判断)
    import subprocess
    disk = subprocess.getoutput('dir')
    info = {'hostname':'c1','memory':disk}

    # 2. 日志处理（堆栈信息）

    # 3. 唯一标记问题
    # 如果只是物理机：sn做唯一标记
    # 物理+虚拟机：1. 系统+调用openstack api ；2.主机名做唯一标记

    url = "http://127.0.0.1:8000/api/asset/"
    r1 = requests.post(
        url=url,
        data=json.dumps(info).encode('utf-8'),
        # data={'k1':'v1','k2':'v2'} # hostname=c1&memory=xxxxx
    )
    print(r1.text)



def task(host):
    # 每一台主机，调用ssh或salt接口远程连接上主机并执行命令 获取结果。（线程池的方式进行采集）
    info = {'hostname': host, 'disk': '....'}
    # 通过requests发送POST请求将资产数据提交到api
    url = "http://127.0.0.1:8000/api/asset/"
    r1 = requests.post(
            url=url,
            data=json.dumps(info).encode('utf-8'),
    )
    print(r1.text)


def ssh():

    # 1. 获取未采集服务器列表
    r1 = requests.get(url="http://127.0.0.1:8000/api/asset/")
    # print(r1.content, r1.text, r1.json() )
    host_list = r1.json()

    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(10)
    for host in host_list:
        pool.submit(task,host)


ssh()