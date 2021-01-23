import numpy as np
import math


def image_translate(origin, destination):
    """
    :param origin:[[x1, y1], [x2, y2], ...]
    :param destination: [[x1', y1'], [x2', y2'], ...]
    :return: k, alpha, dx, dy
    """
    ori = np.array(origin, dtype=np.float64).T
    des = np.array(destination, dtype=np.float64).T
    ori_x = ori[0]
    ori_y = ori[1]
    des_x = des[0]
    des_y = des[1]
    avg_ori_x = ori_x.mean()
    avg_ori_y = ori_y.mean()
    avg_des_x = des_x.mean()
    avg_des_y = des_y.mean()
    ori_xx = ori_x - avg_ori_x
    ori_yy = ori_y - avg_ori_y
    des_xx = des_x - avg_des_x
    des_yy = des_y - avg_des_y
    above = np.sum(np.subtract(np.multiply(ori_xx, des_yy), np.multiply(ori_yy, des_xx)))
    below = np.sum(np.add(np.multiply(ori_xx, des_xx), np.multiply(ori_yy, des_yy)))
    if below == 0:
        temp = np.array([[_cul_min(-90, above, below), _cul_min(90, above, below)], [-90, 90]])
        alpha = temp[1][np.argmin(temp[0])]
    else:
        belta = math.degrees(math.atan(above/below))
        temp = np.array([[_cul_min(belta, above, below), _cul_min(belta + 180, above, below)],
                         [belta, belta + 180]])
        alpha = temp[1][np.argmin(temp[0])]
    k = -_cul_min(alpha, above, below)/np.sum(np.add(np.multiply(ori_xx, ori_xx), np.multiply(ori_yy, ori_yy)))
    dx = avg_des_x + avg_ori_y * k * math.sin(math.radians(alpha)) - avg_ori_x * k * math.cos(math.radians(alpha))
    dy = avg_des_y - avg_ori_y * k * math.cos(math.radians(alpha)) - avg_ori_x * k * math.sin(math.radians(alpha))
    return alpha, k, dx, dy


def _cul_min(alpha, above, below):
    """
    :param alpha: rotate angle
    :param above: var in image_translate
    :param below: var in image_translate
    :return: minimize of loss
    """
    return -(math.sin(math.radians(alpha)) * above.sum() + math.cos(math.radians(alpha)) * below.sum())


def validate(origin, destination, alpha, kk, dx, dy):
    """
    :param origin: [[x1, y1], [x2, y2], ...]
    :param destination: [[x1', y1'], [x2', y2'], ...]
    :param alpha: rotate angle
    :param kk: rate of enlarge
    :param dx: move on road x
    :param dy: move on road y
    :return: minimize of loss
    """
    ori = np.array(origin, dtype=np.float64)
    des = np.array(destination, dtype=np.float64).T
    des_x = des[0]
    des_y = des[1]
    index_x = np.array([[kk * math.cos(math.radians(alpha))], [-kk * math.sin(math.radians(alpha))]], dtype=np.float64)
    index_y = np.array([[kk * math.sin(math.radians(alpha))], [kk * math.cos(math.radians(alpha))]], dtype=np.float64)
    xx = np.dot(ori, index_x) + dx
    yy = np.dot(ori, index_y) + dy
    x2 = des_x - xx.flatten()
    y2 = des_y - yy.flatten()
    result_matrix = np.sqrt(np.add(np.multiply(x2, x2), np.multiply(y2, y2)))
    result = np.sum(result_matrix)
    return result


if __name__ == '__main__':
    a, kkk, x, y = image_translate([[1, 2], [1, 3], [2, 2]], [[1, 2], [0, 2], [1, 3]])
    print(validate([[1, 2], [1, 3], [2, 2]], [[1, 2], [0, 2], [1, 3]], a, kkk, x, y))