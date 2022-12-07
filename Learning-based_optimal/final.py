import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.optimizers import SGD
from keras.losses import MeanSquaredError
from typing_extensions import OrderedDict


# Our examples for an exclusive OR.
def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    # plt.gca().set_ylim(0, 1)
    plt.show()


def Loss(y_true, y_pred):
    y_true = tf.cast(y_true, dtype=tf.float32)
    y_pred = tf.cast(y_pred, dtype=tf.float32)
    return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1))


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
        # # tp[int(math.log2(int(cur[1])))] += 1
        # xxx.append(tp)
        xxx.append([int(cur[1])])
    return [xxx, yyy]

def getModel():
    model = Sequential()
    num_neurons = 40
    model.add(Dense(num_neurons, activation='ReLU', input_dim=1))
    model.add(Dense(num_neurons, activation='ReLU'))
    model.add(Dense(num_neurons, activation='ReLU'))
    model.add(Dense(num_neurons, activation='ReLU'))
    model.add(Dense(num_neurons, activation='ReLU'))
    model.add(Dense(num_neurons, activation='ReLU'))
    model.add(Dense(1))
    model.summary()

    adam = Adam(lr=0.00001)
    model.compile(loss='mean_squared_error', optimizer=adam, metrics=['accuracy'])
    return model

def train(x_train, y_train, model):
    # print(model.predict(x_train))
    history = model.fit(x_train, y_train, batch_size=64, epochs=10)
    # for step in range(4000):
    #     train_cost = model.train_on_batch(x_train, y_train)
    #     if step % 500 == 0:
    #         print('train_cost:', train_cost)
    # plot_learning_curves(history)
    return history


if __name__ == '__main__':
    path = r"E:\DeskTop\res"
    path1 = r"E:\DeskTop\res\element"
    path2 = r"E:\DeskTop\res\base"
    path3 = r"E:\DeskTop\res\net"
    path4 = r"E:\DeskTop\res\test"
    p = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # rr = train([[0 for i in range(32)] for j in range(10)], [i for i in range(0, 10)])
    # print(rr[0])
    x = []
    y = []
    for i in p[0:10]:
        mod = getModel()
        for j in range(1, 3):
            [xx, yy] = read(path + "\\" + str(i) + "ret" + str(j) + ".txt")
            # [test_xx, test_yy] = read(path4 + "\\" + str(i) + "ret" + str(1) + ".txt")
            # for k in range(len(xx)):
            #     x.append(xx[k])
            #     y.append(yy[k])
            train(xx, yy, mod)
        [xx, yy] = read(path + "\\" + str(i) + "ret1" + ".txt")
        res = mod.predict(xx)
        real = [i[0] for i in yy]
        pre = [i[0] for i in res]
        write(path3 + "\\" + str(i) + "ret1" + ".txt", real, pre)
