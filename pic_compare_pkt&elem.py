import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def ARE_line_chart(x, y1, y2):
    plt.plot(x, y1, 'bo-', alpha=0.5, linewidth=2, label='包级别采样')
    plt.plot(x, y2, 'ro-', alpha=0.5, linewidth=2, label='元素级别采样')
    plt.legend()  # 显示上面的label
    plt.title("ARE误差对比")
    plt.xlabel('采样率')
    plt.ylabel('ARE误差')

    plt.show()

def Throughout_line_chart(x, y1, y2):
    plt.plot(x, y1, 'bo-', alpha=0.5, linewidth=2, label='包级别采样')
    plt.plot(x, y2, 'ro-', alpha=0.5, linewidth=2, label='元素级别采样')
    plt.legend()  # 显示上面的label
    plt.title("吞吐量对比")
    plt.xlabel('采样率')
    plt.ylabel('吞吐量(mmps)')
    plt.show()


if __name__ == '__main__':
    p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    pkt_are = [3.84, 2.66, 2.04, 1.70, 1.46, 1.31, 1.13, 1.01, 0.95, 0.87]
    elem_are = [4.91, 2.84, 2.12, 1.67, 1.38, 1.24, 1.11, 1.01, 0.93, 0.87]
    pkt_throughout = [55.2396, 32.6223, 23.8228, 18.8094, 16.8121, 13.5889, 11.8804, 10.5555, 9.51766, 8.441]
    elem_throughout = [27.416, 20.5525, 17.3998, 14.7123, 12.4634, 11.4325, 10.3262, 9.35439, 8.50448, 8.441]
    ARE_line_chart(p, pkt_are, elem_are)
    Throughout_line_chart(p, pkt_throughout, elem_throughout)