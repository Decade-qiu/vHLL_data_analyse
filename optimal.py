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
    print(min(y), max(y), min(x1), max(x1))
    return [y, x1, x2, x3]


# 需要拟合的函数
def f(x, A, B, C, D):
    return A * x ** 3 + B * x ** 2 + C * x + D

def fx(x, A, B, C, D):
    return A * x ** 3 + B * x ** 2 + C * x + D

def optimal(x_group, y_group):
    # 得到返回的A，B值
    A, B, C, D = op.curve_fit(f, x_group, y_group)[0]
    # print(A, B, C, D)
    # 数据点与原先的进行画图比较
    plt.scatter(x_group, y_group, s=80, marker='x', label='真实值')
    x = np.arange(1, 14000, 0.01)
    y = fx(x, A, B, C, D)
    plt.plot(x, x, color='red', label='拟合曲线')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()  # 显示label
    plt.show()
    return [A, B, C, D]


if __name__ == '__main__':
    path = r"E:\DeskTop\res"
    # x = dd(r"E:\DeskTop\res\base\50ret1.txt")
    # optimal(x[0], x[1])
    # draw.diff_ARE(x[0], x[1])
    p = [10, 30, 50, 80, 100]
    plt.figure()
    file = open(path + "cov.txt", 'w')
    for i in p:
        print("===================P = " + str(i) + " ====================")
        cov = [0, 0, 0, 0]
        for j in range(1, 6):
            real_ave = dd(path + "\\100" + "ret" + str(j) + ".txt")[2]
            [real, nf, ave, p] = dd(path + "\\" + str(i) + "ret" + str(j) + ".txt")
            tp = optimal(ave, real_ave)
            print(tp)
            cov = [i+j for i, j in zip(cov, tp)]
        print("===========================================================")
        cov = [i/5 for i in cov]
        print(cov)
        file.write(str(cov[0])+" "+str(cov[1])+" "+str(cov[2])+" "+str(cov[3])+"\n")
    file.close()
