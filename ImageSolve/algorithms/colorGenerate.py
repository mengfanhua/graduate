import numpy as np
import math


def ColorGenerate(value):
    """
    通过颜色图的扩展，获得黑白色与颜色图的立体图，通过螺旋方法获得颜色点
    :param value: the number of point * 240 / 45
    :return:color: calculated color
    """
    x = round(value * math.sin(value) / 2) + 120
    y = round(value * math.cos(value) / 4) + 60
    print(x, y)
    max_sum = 255 - round(y * 128 / 240.0)
    min_sum = round(y * 127 / 240.0)
    if x < 40:
        te = np.array([max_sum, min_sum + round(x * (max_sum - min_sum) / 40.0), min_sum])
    elif x < 80:
        te = np.array([max_sum - round((x-40) * (max_sum - min_sum) / 40.0), max_sum, min_sum])
    elif x < 120:
        te = np.array([min_sum, max_sum, min_sum + round((x - 80) * (max_sum - min_sum) / 40.0)])
    elif x < 160:
        te = np.array([min_sum, max_sum - round((x - 120) * (max_sum - min_sum) / 40.0), max_sum])
    elif x < 200:
        te = np.array([min_sum + round((x - 160) * (max_sum - min_sum) / 40.0), min_sum, max_sum])
    else:
        te = np.array([max_sum, min_sum, max_sum - round((x - 200) * (max_sum - min_sum) / 40.0)])
    if value < 120:
        temp = np.array([255, 255, 255])
        color = (temp - te) * (120 - value) / 120 + te
    else:
        color = te - te * (value - 120) / 120
    return color


def ColorTranslate(color):
    """
    translate color(np.array) to hex(example: #ffffff)
    :param color:
    :return:
    """
    return "#" + toHex(int(max(min(255, color[0]), 0))) + \
           toHex(int(max(min(255, color[1]), 0))) +\
           toHex(int(max(min(255, color[2]), 0)))


def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hexStr = ""

    if num < 0:
        num = num + 2 ** 32

    while num >= 16:
        digit = num % 16
        hexStr = chaDic.get(digit, str(digit)) + hexStr
        num //= 16
    hexStr = chaDic.get(num, str(num)) + hexStr
    while len(hexStr) < 2:
        hexStr = "0" + hexStr
    return hexStr

