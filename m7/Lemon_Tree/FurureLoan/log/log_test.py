"""
Time    : 2019/3/29 17:04
Author  : wang xin
Email   : 452427904@qq.com
File    : log_test.py
"""

import logging

# 创建收集日志的容器，并设置收集日志的等级
# 收集日志需要1、创建日志容器，2、创建输出渠道，3、容器和渠道对接
logger = logging.getLogger('my_logger')
logger.setLevel('INFO')

formatter = logging.Formatter('%(asctime)s %(filename)s %(leveltime)s %(name)s %(message)s')


ch = logging.StreamHandler()
logger.addHandler(ch)

ch.setFormatter(formatter)

logger.info('info')
logger.warning('warning')