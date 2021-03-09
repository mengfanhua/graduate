import numpy as np
from ImageSolve.algorithms.converterZ import Zconverter


def exchangeType(ori):
    a = np.array(ori)[:, 1:]
    return a


def exchangeTile(des, value):
    result = []
    for i in range(len(des)):
        a, b = Zconverter(des[i][0], value, des[i][1], des[i][2])
        result.append([a, b])
    return result
