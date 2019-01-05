#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor


def task(host):
    """
    采集资产
    :return:
    """
    time.sleep(2)
    print(host)

# 创建了一个线程池，线程池中最多放20个线程（20个我去采集资产）
pool = ThreadPoolExecutor(20)

for i in range(1,101):
    hostname = "c%s.com" %(i,)
    # 去线程池中申请一个线程去执行task函数
    pool.submit(task,hostname)