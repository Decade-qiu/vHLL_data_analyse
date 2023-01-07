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

def Throughout_are_chart(x1, x2, y1, y2):
    plt.plot(x1, y1, 'bo-', alpha=0.5, linewidth=2, label='包级别采样')
    plt.plot(x2, y2, 'ro-', alpha=0.5, linewidth=2, label='元素级别采样')
    plt.legend()  # 显示上面的label
    plt.title("平均包处理时间 VS ARE")
    plt.xlabel('平均包处理时间(ns)')
    plt.ylabel('ARE')
    plt.show()


if __name__ == '__main__':
    p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    pkt_are = [0.74, 0.64, 0.55, 0.67, 0.62, 0.64, 0.55, 0.37, 0.54, 0.52]
    elem_are = [9.49, 5.07, 3.85, 3.20, 2.66, 2.26, 1.94, 1.69, 1.46, 1.32]
    pkt_throughout = [63.5377, 38.3241, 24.3151, 21.4161, 17.8536, 15.9601, 12.2875, 10.9416, 9.84191, 8.441]
    elem_throughout = [30.1269, 22.7895, 18.8317, 16.0121, 13.2273, 12.1345, 10.8738, 10.5246, 9.2942, 8.441]
    ARE_line_chart(p, pkt_are, elem_are)
    Throughout_line_chart(p, pkt_throughout, elem_throughout)
    pkt_processTime = [1/i for i in pkt_throughout]
    elem_processTime = [1/i for i in elem_throughout]
    Throughout_are_chart(pkt_processTime, elem_processTime, pkt_are, elem_are)
