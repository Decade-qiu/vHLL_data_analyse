import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as op
import draw

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def dd(path):
    file = open(path, 'r')
    data = file.readlines()
    x1 = []
    x2 = []
    x3 = []
    y = []
    for d in data:
        cur = d.split(" ")
        v1 = int(cur[0])
        v2 = int(cur[1])
        v3 = float(cur[2])
        # v4 = float(cur[3][:-1])
        x1.append(v2)
        x2.append(v3)
        # x3.append(v4)
        y.append(v1)
    # print(min(y), max(y), min(x1), max(x1))
    return [y, x1, x2, x3]


# 需要拟合的函数
def f(x, A, B, C, D, E):
    return A * x ** 4 + B * x ** 3 + C * x ** 2 + D * x + E


def fx(x, A, B, C, D, E):
    return A * x ** 4 + B * x ** 3 + C * x ** 2 + D * x + E


def residuals(A, B, C, D, E, y, x):
    y0 = A * x ** 4 + B * x ** 3 + C * x ** 2 + D * x + E
    return abs(y - y0) / y


def optimal(x_group, y_group, title, show):
    # fig = plt.figure()
    # A, B, C, D, E = op.curve_fit(f, x_group, y_group)[0]
    z1 = np.polyfit(x_group, y_group, 7)
    p1 = np.poly1d(z1)
    # print(z1)
    # 数据点与原先的进行画图比较
    plt.scatter(x_group, y_group, s=80, marker='+', label='散点图')
    x = np.arange(1, 14000, 0.01)
    y = p1(x)
    # plt.plot(x, x, label='y = x')
    plt.plot(x, y, label='拟合曲线')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()  # 显示label
    plt.title(title)
    if show == 1:
        plt.show()
    # draw.diff_ARE(x_group, y_group)
    # draw.diff_MAE(x_group, y_group)
    return z1


def get(opt, x):
    res = ''
    if opt > 0:
        res = '+'
    res += str(opt)
    for i in range(x):
        res += "*nf"
    return res


if __name__ == '__main__':
    path = r"E:\DeskTop\res"
    path1 = r"E:\DeskTop\res\element"
    path2 = r"E:\DeskTop\res\base"
    # P = 100
    # x = dd(path + "\\" + str(P) + "ret1.txt")
    # # y = dd(path1 + "\\"+str(P)+"ret1.txt")
    # # print(len(x[0]), len(y[0]))
    # optimal(x[0], x[1], "包级别采样")
    # # optimal(y[0], y[1], "元素级别采样")
    p = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    file = open(path + "cov.txt", 'w')
    for i in p[0:1]:
        print("===================P = " + str(i) + "=================================")
        cov = [0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(1, 6):
            # real_ave = dd(path + "\\100" + "ret" + str(j) + ".txt")[2]
            res = dd(path + "\\" + str(i) + "ret" + str(j) + ".txt")
            tp = optimal(res[1], res[0], "", 0)
            cov = [i + j for i, j in zip(cov, tp)]
        cov = [i / 5 for i in cov]
        print(cov)
        cov = [get(cov[i], 7-i) for i in range(8)]
        if i == 10:
            file.write("if (P == 10) nf = ")
        else:
            file.write("else if (P == " + str(i) + ") nf = ")
        file.write(str(cov[0]) + " " + str(cov[1]) + " " + str(cov[2])
                   + " " + str(cov[3]) + " " + str(cov[4]) + " " + str(cov[5])
                   + " " + str(cov[6]) + " " + str(cov[7]) + ";" + "\n")
    file.close()
