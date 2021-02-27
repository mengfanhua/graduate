import math


def Zconverter(ori_z, des_z, ori_x, ori_y):
    """
    :param ori_z: origin zoom in tile
    :param des_z: destination zoom in tile
    :param ori_x: axis=0
    :param ori_y: axis=1
    :return: des_x, des_y
    """
    MCx = ori_x * math.pow(2, 18 - ori_z)
    MCy = (256 - ori_y) * math.pow(2, 18 - ori_z)
    des_x = MCx / math.pow(2, 18 - des_z)
    des_y = MCy / math.pow(2, 18 - des_z)
    return des_x, 256 - des_y
