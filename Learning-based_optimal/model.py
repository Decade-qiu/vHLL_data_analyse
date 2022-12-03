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
        wr.write(str(x[i]) + " " + str(max(1, y[i][0])) + "\n")


def read(path):
    file = open(path, 'r')
    data = file.readlines()
    x = []
    y = []
    for d in data:
        cur = d.split(" ")
        y.append(int(cur[0]))
        tp = []
        for i in range(3, 34):
            tp.append(int(cur[i]))
            # tp[int(cur[i])] += 1
        ns = int(cur[1])
        tp.append(math.log2(ns))
        x.append(tp)
    return [x, y]

def getModel(dim):
    model = Sequential()
    num_neurons = 64
    # model.add(Dense(33, input_dim=dim))
    model.add(Dense(num_neurons, activation='ReLU', input_dim=dim))
    model.add(Dense(num_neurons, activation='ReLU'))
    model.add(Dense(num_neurons, activation='ReLU'))
    model.add(Dense(1))
    model.summary()

    adam = Adam()
    model.compile(loss='mape', optimizer=adam, metrics=['accuracy'])
    return model

def train(x_train, y_train, x_test, y_test, model, save_path):
    # print(model.predict(x_train))
    history = model.fit(x_train, y_train, batch_size=32, epochs=3)
    # plot_learning_curves(history)

    res = model.predict(x_test)
    write(save_path, y_test, res)
    return res


if __name__ == '__main__':
    path = r"E:\DeskTop\res"
    path1 = r"E:\DeskTop\res\element"
    path2 = r"E:\DeskTop\res\base"
    path3 = r"E:\DeskTop\res\net"
    p = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # rr = train([[0 for i in range(32)] for j in range(10)], [i for i in range(0, 10)])
    # print(rr[0])
    x = []
    y = []
    for i in {10, 30, 50, 70, 90}:
        for j in range(3, 4):
            [xx, yy] = read(path + "\\" + str(i) + "ret" + str(j) + ".txt")
            [test_xx, test_yy] = read(path + "\\" + str(i) + "ret" + str(1) + ".txt")
            mod = getModel(len(xx[0]))
            # for k in range(len(xx)):
            #     x.append(xx[k])
            #     y.append(yy[k])
            train(xx, yy, test_xx, test_yy, mod, path3 + "\\" + str(i) + "ret" + str(j) + ".txt")
