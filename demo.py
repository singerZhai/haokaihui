# import os
# import logging
# from time import sleep
#
# path = os.path.dirname(os.path.realpath(__file__))
# print(path)
# demo_path = os.path.join(path, 'demo')
# print(demo_path)
# number = 0
# logger = logging.getLogger()
# ch = logging.StreamHandler()
# formatter = logging.Formatter('[%(asctime)s] - %(levelname)s: %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)
# logger.setLevel(logging.DEBUG)
#
#
# while number <= 100:
#     logger.debug(number)
#     if not os.path.exists(demo_path):
#         os.mkdir(demo_path)
#         logger.info('目录已创建')
#         sleep(1)
#         number += 1
#     else:
#         if os.path.exists(demo_path):
#             os.rmdir(demo_path)
#             logger.info('目录已删除')
#             sleep(1)
#             number += 1
# import shutil
#
# Report_path = './Report/'
# files_count = len(os.listdir(Report_path))
# if files_count > 10:
#      shutil.rmtree(Report_path)
#      os.mkdir(Report_path)
# import datetime
# import time
#
# from jinja2 import runtime
#
# print(datetime.datetime.now())
# print(type(datetime.datetime.now()))
# print(time.time())
# print(type(time.time()))
# print(runtime)
# !/usr/bin/python3
import json
import threading
import time
#
# exitFlag = 0
#
#
# class MyThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)
#
#
# def print_time(thread_name, delay, counter):
#     while counter:
#         if exitFlag:
#             thread_name.exit()
#         time.sleep(delay)
#         print("%s: %s" % (thread_name, time.ctime(time.time())))
#         counter -= 1
#
#
# if __name__ == '__main__':
#
#     # 创建新线程
#     thread1 = MyThread(1, "Thread-1", 1)
#     thread2 = MyThread(2, "Thread-2", 2)
#
#     # 开启新线程
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()
#     print("退出主线程")
from time import sleep

# def demo(int_list):
#     new_list = list()
#     for i in int_list:
#         if i == 6:
#             i = 0
#             new_list.append(i)
#     return new_list
#
#
# def first(method, demo_list):
#     for i in demo_list:
#         print(i)
#         sleep(1)
#     return method(demo_list)
#
#
# demo_list = [6, 6, 6, 6, 6, 6, 6]
# print(first(demo, demo_list))


# def first(name_list):
#     print(name_list)
#     new_list = list()
#     for i in name_list:
#         if i == '小明':
#             new_list.append(i)
#             print('小明下标' + str(name_list.index(i)))
#             continue
#         else:
#             if i not in new_list:
#                 new_list.append(i)
#                 print('Hello:' + i)
#                 sleep(1)
#     return new_list
#
#
# name_list = ['小红', '小樱', '小花', '小明', '小刚', '小刚']
# a = first(name_list)
# print(a)
import requests

from base.base_action import get_url, get_params

# login_url = get_url('data', 'login', 'url')
# login_params = get_params('data', 'login', 'params')
# r = requests.post(url=login_url, data=login_params)
# res = r.json()
# print(type(res))
# print(res)
# result = json.dumps(res, ensure_ascii=False)
# print(type(result))
# print(result)
# res = {'status': 200, 'msg': '请求成功', 'errorResult': None, 'data': {'userToken': 'f706e1634dfd09ad5ad54bdfb8cc4bab', 'user': {'userid': 73286, 'usertype': 1, 'isInnerUser': 0, 'username': '15611066631', 'password': 'e10adc3949ba59abbe56e057f20f883e', 'realname': None, 'nickname': '翟', 'deviceUdid': None, 'mobile': '15611066631', 'email': None, 'sex': '0', 'headimage': None, 'birthday': None, 'profession': None, 'education': None, 'homeAddress': None, 'livingAddress': None, 'openid': None, 'userToken': 'f706e1634dfd09ad5ad54bdfb8cc4bab', 'source': '3', 'isAgentRecommend': 0, 'agentId': None, 'times': 52, 'sumTimes': 0, 'usedTimes': 0, 'packageEnddate': None, 'lastRegid': '', 'lastRegidType': None, 'lastLoginTime': 1544930383782, 'createTime': 1544016864000, 'lastModifyTime': 1544930383782, 'status': 1}, 'deviceList': [{'deviceid': 14, 'devicetypeid': 1, 'entid': 1, 'officeid': 0, 'devicename': '通讯服务器', 'position': '', 'sipserverip': '47.95.29.36', 'sipport': 28518, 'sippassword': '180', 'registerexpires': 60, 'rights': 100, 'monitorimg': None, 'deviceimg': None, 'note': '', 'status': '1'}]}}
# print(type(res))
# result = json.dumps(res, ensure_ascii=False)
# print(result)
