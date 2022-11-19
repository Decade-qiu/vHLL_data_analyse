import os
import time

import torch
import torchvision.datasets
from torch import nn
import os.path
from scapy.all import *
from scapy.layers.inet import IP
from random import random
from mmh3 import hash, hash64, hash128
from vHLL import vHLL


def calc(N, M, P, data, idx):
    # vHLL类 N是物理寄存器长度 M是分桶的数量
    vhll = vHLL(N, M)
    dic = {}
    flow = set()
    file = open(data, 'r')
    total = file.readlines()
    print("实际流数量：", len(total))
    smp = 0
    for ip in total:
        lst = ip.split(" ")
        src = lst[0]
        dst = lst[1][:-1]
        if src not in flow:
            flow.add(src)
            dic[src] = set()
        dic[src].add(dst)
        # 前置包级别采样 小于p则采样
        r = random()
        if r < P:
            smp += 1
            vhll.insert(src, dst)  # vHLL插入
    file.close()
    n = vhll.totalCardinality()
    size = r"E:\DeskTop\res\size" + str(idx) + ".txt"
    wr = open(size, 'w')
    real_size = 0
    for ip in flow:
        wr.write(ip+" ")
        s = len(dic[ip])
        real_size += s
        wr.write(str(s)+" ")  # 实际的基数
        wr.write(str(vhll.query(ip, n))+"\n")  # vHLL估计的基数
    print("采样流数量：", smp)
    print(len(flow), real_size, n)


def real_total():
    pp = r"E:\DeskTop\res"
    data = os.listdir(pp)
    for tt in data:
        file = open(os.path.join(pp, tt), 'r')
        data = file.readlines()
        xl = 0
        yl = 0
        print(len(data), end=" ")
        for d in data:
            cur = d.split(" ")
            v1 = int(cur[1])
            v2 = int(cur[2][:-1])
            xl += v1
            yl += v2
        print(xl, yl)


if __name__ == '__main__':
    path = r"E:\DeskTop\train"
    idx = 1
    MB1 = 1677722
    KB256 = 419430
    KB128 = 209715
    t1 = time.clock()
    for txt in os.listdir(path):
        calc(MB1, 32, 0.8, os.path.join(path, txt), idx)
        idx += 1
    t2 = time.clock()
    print("用时:", (t2-t1)*1000000)
    # real_total()
    # x = 0
    # for i in range(100000):
    #     r = random()
    #     if r < 0.01:
    #         x += 1
    # print(x)
