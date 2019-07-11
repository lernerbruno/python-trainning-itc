#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:46:46 2019

@author: nadavnehmadi
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
Y = np.array([[0], [1], [1], [0]])

epochs = 10000
inputLayerSize = 3
hiddenLayerSize = 3
outputLayerSize = 1


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_(x):
    return sigmoid(x) * (1 - sigmoid(x))


Wh = np.random.uniform(size=(inputLayerSize, hiddenLayerSize))
Wz = np.random.uniform(size=(hiddenLayerSize, outputLayerSize))

for i in range(epochs):
    L1 = np.dot(X, Wh)
    H = sigmoid(L1)
    L2 = np.dot(H, Wz)
    Z = sigmoid(L2)
    E = Y - Z
    dZ = sigmoid_(L2) * E
    dH = sigmoid_(L1) * dZ.dot(Wz.T)
    Wz += np.dot(H.T, dZ)
    Wh += np.dot(X.T, dH)
print(Z)  # what have we learn?
