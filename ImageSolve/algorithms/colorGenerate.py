import numpy as np
import math

colorList = [(136, 0, 21), (237, 28, 36), (255, 127, 39), (255, 242, 0), (34, 177, 76),
             (0, 162, 232), (63, 72, 204), (163, 73, 164), (185, 122, 87),
             (255, 174, 201), (255, 201, 14), (239, 228, 176), (181, 230, 29),
             (153, 217, 234), (112, 146, 190), (200, 191, 231)]


def ColorGenerate(value):
    """
    :param value: the number of point * 240 / 45
    :return:color: calculated color
    """
    global colorList
    return colorList[(value - 1) % len(colorList)]


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

