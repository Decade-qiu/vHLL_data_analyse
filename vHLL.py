# import math
# import os
# import torch
# import torchvision.datasets
# from torch import nn
# import os.path
import math

from scapy.all import *
# from scapy.layers.inet import IP
# import random
from mmh3 import hash, hash64, hash128

class vHLL(object):

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.b = int(math.log(M, 2))
        self.array = [0 for i in range(N)]

    def getAlpha(self, t):
        if t == 16:
            return 0.673
        elif t == 32:
            return 0.697
        elif t == 64:
            return 0.709
        return 0.7213 / (1 + 1.079 / t)

    def getBeta(self, ez):
        zl = math.log(ez + 1, math.pi)
        return -0.370393911 * ez + 0.070471823 * zl + 0.17393686 * math.pow(zl, 2) + 0.16339839 * math.pow(zl,
                                                                                                           3) - 0.09237745 * math.pow(
            zl, 4) + 0.03738027 * math.pow(zl, 5) - 0.005384159 * math.pow(zl, 6) + 0.00042419 * math.pow(zl, 7)

    def H(self, ip):
        return hash(str(ip), 1377, signed=False)

    def first_one_bit(self, bin_ip):
        dx = 0
        for i in bin_ip:
            if i == '1':
                break
            dx += 1
        return dx + 1

    def enCode(self, ip32):
        bin_v = "{0:b}".format(ip32).zfill(32)
        p = ip32 % self.M
        q = self.first_one_bit(bin_v[::-1][self.b:])
        return [p, q]

    def insert(self, src, dst):
        e32 = self.H(dst)
        f32 = self.H(src)
        [p, q] = self.enCode(e32)
        index = self.H(f32 ^ p) % self.N
        prev = self.array[index]
        if prev < q:
            self.array[index] = q

    def totalCardinality(self):
        sum_t = 0.0
        zero = 0
        for i in range(self.N):
            if self.array[i] == 0:
                zero += 1
            sum_t += 1.0 / pow(2, self.array[i])
        # beta = getBeta(zero)
        # return getAlpha(N) * N * (N - zero) / (sum_t + beta)
        return self.getAlpha(self.N) * self.N * self.N / sum_t

    def query(self, src, n):
        f32 = self.H(src)
        sum_t = 0.0
        zero = 0
        for i in range(self.M):
            index = self.H(f32 ^ i) % self.N
            if self.array[index] == 0:
                zero += 1
            sum_t += 1.0 / pow(2, self.array[index])
        # beta = getBeta(zero)
        # ns = getAlpha(M) * M * (M - zero) / (sum_t + beta)
        ns = self.getAlpha(self.M) * self.M * self.M / sum_t
        if ns < 2.5 * self.M and zero != 0:
            ns = -self.M * math.log2(zero / self.M)

        # nf = ns - (M * n / N)
        nf = (self.N*self.M/(self.N-self.M))*(ns/self.M-n/self.N)

        # nf = abs(nf)

        return round(nf + 0.5)

if __name__ == '__main__':
    # print(enCode(H("192.168.1.1")))
    print(math.log(64, 2))
    aa = random.randint(1, 1000000000)
    bb = random.randint(1, 1000)
    y = str(aa) + ".!%^@.[.[" + str(bb) + "."
    print(hash(y, 1000, signed=False))
    for j in range(6):
        print(hash(y, 1000, signed=False), end=" ")
    print()
