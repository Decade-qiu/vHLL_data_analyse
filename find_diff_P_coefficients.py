import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as op
import draw

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 需要拟合的函数
def f(x, A, B, C, D, E):
    return A * x ** 4 + B * x ** 3 + C * x ** 2 + D * x + E


def fx(x, A, B, C, D, E):
    return A * x ** 4 + B * x ** 3 + C * x ** 2 + D * x + E


def get_factor(x_group, y_group, show):
    # fig = plt.figure()
    z1 = np.polyfit(x_group, y_group, 3)
    p1 = np.poly1d(z1)
    x = np.array([i / 10 for i in range(1, 11)])
    y = p1(x)
    if show == 1:
        plt.show()
    # draw.diff_ARE(x_group, y_group)
    # draw.diff_MAE(x_group, y_group)
    return y


def get(opt, x):
    res = ''
    if opt > 0:
        res = '+'
    res += str(opt)
    for i in range(x):
        res += "*ave"
    return res


if __name__ == '__main__':
    path = r"E:\DeskTop\respcov.txt"
    ret = r"E:\DeskTop\res.txt"
    f = open(path, 'r')
    d = f.readlines()
    f.close()
    lst = [[], [], [], [], [], []]
    for l in d:
        arr = l.split(" ")
        arr[5] = arr[5].strip()
        for i in range(6):
            lst[i].append(float(arr[i]))
    p = [0.1, 0.3, 0.5, 0.8, 1.0]
    res_factor = []
    for i in lst:
        res_factor.append(get_factor(p, i, 0))
    res = open(ret, 'w')
    for i in range(10):
        cov = [res_factor[j][i] for j in range(6)]
        cov = [get(cov[j], 5 - j) for j in range(6)]
        res.write(str(cov[0]) + " " + str(cov[1]) + " " + str(cov[2])
                  + " " + str(cov[3]) + " " + str(cov[4]) + " " + str(cov[5]) + "\n")
    res.close()
