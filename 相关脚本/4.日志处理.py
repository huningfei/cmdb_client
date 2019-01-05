#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging

# 方式一：
"""
logging.basicConfig(filename='log1.log',
                    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10)

logging.info('info,asdfasdfasdfasdf')
logging.error('error,asdfasdfasdf')
"""

# 方式二：

file_handler = logging.FileHandler('xxxxxxxx.log', 'a', encoding='utf-8')
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s:  %(message)s"))

logger = logging.Logger('s1', level=logging.INFO)
logger.addHandler(file_handler)

logger.info('1111')
logger.error('2222')
