import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
from torch.autograd import Variable


def write(p, x, y):
    wr = open(p, 'w')
    for i in range(len(x)):
        wr.write(str(x[i]) + " " + str(max(1, y[i])) + "\n")


def read(path):
    file = open(path, 'r')
    data = file.readlines()
    xxx = []
    yyy = []
    for d in data:
        cur = d.split(" ")
        yyy.append([int(cur[0])])
        # tp = [0 for ii in range(28)]
        # for ii in range(3, 34):
        #     tp[int(cur[i])] += 1
        #     # tp[int(cur[i])] += 1
        # tp[int(math.log2(int(cur[1])))] += 1
        xxx.append([int(cur[1])])
    return [xxx, yyy]


class Net(nn.Module):
    def __init__(self, n_input, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden1 = nn.Linear(n_input, n_hidden)
        self.hidden2 = nn.Linear(n_hidden, n_hidden)
        self.hidden2 = nn.Linear(n_hidden, n_hidden)
        self.predict = nn.Linear(n_hidden, n_output)

    def forward(self, input):
        out = self.hidden1(input)
        out = F.relu(out)
        out = self.hidden2(out)
        out = F.sigmoid(out)
        out = self.predict(out)
        return out


def train(net, xx, yy):
    x = Variable(torch.tensor(xx, dtype=torch.float))
    y = Variable(torch.tensor(yy, dtype=torch.float))
    print(net)
    optimizer = torch.optim.Adam(net.parameters(), lr=0.01)
    loss_func = torch.nn.MSELoss()
    plt.ion()
    plt.show()
    for t in range(30):
        prediction = net(x)
        loss = loss_func(prediction, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # if t % 2 == 0:
        #     plt.cla()
        #     plt.scatter(x.data.numpy(), y.data.numpy())
        #     plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        #     plt.text(0.5, 0, 'Loss = %.4f' % loss.data, fontdict={'size': 20, 'color': 'red'})
        #     plt.pause(0.05)
    plt.ioff()
    plt.show()


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
    for i in p[0:5]:
        net = Net(1, 25, 1)
        for j in range(1, 2):
            [xx, yy] = read(path + "\\" + str(i) + "ret" + str(j) + ".txt")
            # [test_xx, test_yy] = read(path4 + "\\" + str(i) + "ret" + str(1) + ".txt")
            # for k in range(len(xx)):
            #     x.append(xx[k])
            #     y.append(yy[k])
            train(net, xx, yy)
            # plt.scatter(xx, yy)
            # plt.show()
        [xx, yy] = read(path + "\\" + str(i) + "ret1" + ".txt")
        x = Variable(torch.tensor(xx, dtype=torch.float))
        res = net(x)
        real = [i[0] for i in yy]
        pre = [i[0] for i in res]
        write(path3 + "\\" + str(i) + "ret1" + ".txt", real, pre)
