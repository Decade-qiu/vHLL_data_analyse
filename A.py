import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def Throughout_line_chart(x, y1):
    plt.plot(x, y1, 'bo-', alpha=0.5, linewidth=2)
    # plt.plot(x, y2, 'ro-', alpha=0.5, linewidth=2, label='元素级别采样')
    plt.legend()  # 显示上面的label
    plt.title("author：仇忠骏")
    plt.xlabel('RTT')
    plt.ylabel('拥塞窗口 cwnd')
    x_major_locator = MultipleLocator(2)
    # 把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(4)
    # 把y轴的刻度间隔设置为10，并存在变量里
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    plt.show()

if __name__ == '__main__':
    x = [i for i in range(1, 27)]
    y = [1, 2, 4, 8, 16, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 21, 22, 23, 24, 25, 26, 1, 2, 4, 8]
    Throughout_line_chart(x, y)