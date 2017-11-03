#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

def qiuzhushi(num):
    listData = range(2, num, 1)
    # 保留的数组
    listzhishu = []
    # 从原来的数组中去除的部分
    listExcept = []
    c = listData
    while c:
        # 每次遍历需要去除的部分
        listNotIn = []
        # 每次留下来的，第一位都是质数
        z = c[0];
        listzhishu.append(z);
        while z < num+1:
            listNotIn.append(z)
            for k in listExcept:
                if k * z < num+1:
                    listNotIn.append(k * z)
            z = c[0] * z
        listExcept += listNotIn
        b = set(listData) - set(listExcept)
        c = list(b)
        c.sort()
    return listzhishu

def qiuzhishuList(num):
    listData = range(3,num,1)
    c = listData
    listzhishu = [2]
    for i in listData :
        zhishu = []
        for k in listzhishu:
            if i%k != 0:
                if k ==listzhishu[-1]:
                    zhishu.append(i)
            else:
                break
        listzhishu.extend(zhishu)

    return listzhishu
# listData = range(2, 10000, 1);
# # 保留的数组
# listzhishu = []
# # 从原来的数组中去除的部分
# listExcept = []
# c = listData
# while c:
#     # 每次遍历需要去除的部分
#     listNotIn = []
#     # 每次留下来的，第一位都是质数
#     z = c[0];
#     listzhishu.append(z);
#     while z < 10001:
#         listNotIn.append(z)
#         for k in listExcept:
#             if k * z < 10001:
#                 listNotIn.append(k * z)
#         z = c[0] * z
#     listExcept += listNotIn
#     b = set(listData) - set(listExcept)
#     c = list(b)
#     c.sort()
print time.time()
print "qiuzhushi "
print qiuzhushi(1000000)
# print "qiuzhishuList"
# print qiuzhishuList(1000000)
print time.time()

# while(list):
