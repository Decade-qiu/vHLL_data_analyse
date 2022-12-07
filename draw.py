import os

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
from scipy.interpolate import make_interp_spline


# 返回[xl, yl, AREl] xl：实际基数 yl：估计基数 AREl：总误差
def read_res(path):
    file = open(path, 'r')
    data = file.readlines()
    xl = []
    yl = []
    AREl = 0
    MAXa = 0
    MAXe = 0
    for d in data:
        cur = d.split(" ")
        v1 = int(cur[0])
        v2 = int(cur[1][:-1])
        xl.append(v1)
        yl.append(v2)
        MAXa = max(MAXa, v1)
        MAXe = max(MAXe, v2)
        AREl += abs(v2 - v1) / v1
    AREl = AREl / len(data)
    print(MAXa, MAXe, AREl)
    return [xl, yl, AREl]


# 计算不同基数区间ARE值
def diff_ARE(x, y):
    are = [[], [], [], [], []]
    cnt = 0
    for i in range(len(x)):
        a = x[i]
        b = y[i]
        cnt += abs(a-b)/a
        if a <= 10:
            are[0].append(abs(a - b) / a)
        elif a <= 100:
            are[1].append(abs(a - b) / a)
        elif a <= 1000:
            are[2].append(abs(a - b) / a)
        elif a <= 10000:
            are[3].append(abs(a - b) / a)
        else:
            are[4].append(abs(a - b) / a)
    print("不同基数区间ARE")
    for lst in are:
        if len(lst) == 0:
            print("NULL")
            continue
        print("{:.3f}".format(round(sum(lst) / len(lst), 3)), end="\t")
    print("总ARE:", cnt/len(x))


# 计算不同基数区间平均噪声值（噪声：估计基数-实际基数）
def diff_MAE(x, y):
    noise = [[], [], [], [], []]
    for i in range(len(x)):
        a = x[i]
        err = abs(y[i] - a)
        if a <= 10:
            noise[0].append(err)
        elif a <= 100:
            noise[1].append(err)
        elif a <= 1000:
            noise[2].append(err)
        elif a <= 10000:
            noise[3].append(err)
        else:
            print(a, y[i], err)
            noise[4].append(err)
    for lst in noise:
        if len(lst) == 0:
            print("无")
            continue
        print(round(sum(lst) / len(lst), 3), end="\t")
    print()


def dd(path):
    file = open(path, 'r')
    data = file.readlines()
    x1 = []
    x2 = []
    x3 = []
    y = []
    for d in data:
        cur = d.split(" ")
        v1 = float(cur[0])
        v2 = float(cur[1])
        # v3 = float(cur[2])
        # v4 = float(cur[3][:-1])
        x1.append(v2)
        # x2.append(v3)
        # x3.append(v4)
        y.append(v1)
    # print(min(y), max(y), min(x1), max(x1))
    return [y, x1]


# 画散点图 x y 是横纵坐标的值 savepath是图片保存地址
def draw_scatter(x, y, flag, savepath):
    fig = plt.figure()
    MM = 5
    a = range(0, MM)
    # plt.scatter(x, y, s=50, marker='x')
    plt.plot(np.  log10(x), np.log10(y), "x")
    plt.plot(a, a)
    # plt.xscale('log')
    # plt.yscale('log')
    plt.xlabel("实际基数")
    plt.ylabel("估计基数")
    # diff_ARE(x, y)
    if flag == 1:
        plt.show()
    else:
        plt.savefig(savepath, dpi=300)


def get_ARE(x, y):
    tp = [abs(yyy - xxx) / xxx for xxx, yyy in zip(x, y)]
    print("%.2f" % (sum(tp) / len(tp)), end=', ')


if __name__ == '__main__':
    path = r"E:\DeskTop\res"
    path1 = r"E:\DeskTop\res\element"
    path2 = r"E:\DeskTop\res\base"
    path3 = r"E:\DeskTop\res\net"
    path4 = r"E:\DeskTop\res\test"
    # P = 60
    # x = dd(path1 + "\\" + str(P) + "ret1.txt")
    # # y = dd(path1 + "\\"+str(P)+"ret1.txt")
    # # print(len(x[0]), len(y[0]))
    # draw_scatter(x[0], x[1], 1, "")
    # get_ARE(x[0], x[1])
    # # optimal(y[0], y[1], "元素级别采样")
    p = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in p[0:1]:
        xx = dd(path + "\\" + str(10) + "ret1" + ".txt")
        # draw_scatter(xx[0], xx[1], 0, r"E:\DeskTop\pic\修正_elem_real_esi" + "\\" + str(i) + ".png")
        # draw_scatter(xx[0], xx[1], 0, r"E:\DeskTop\pic\real_esi" + "\\" + str(i) + ".png")
        draw_scatter(xx[0], xx[1], 1, r"E:\DeskTop\pic\神经网络修正_pkt_real_esi" + "\\" + str(i) + ".png")
        # draw_scatter(xx[0], xx[1], 0, r"E:\DeskTop\pic\测试集_pkt_real_esi" + "\\" + str(i) + ".png")
        get_ARE(xx[0], xx[1])
        # diff_ARE(xx[0], xx[1])
