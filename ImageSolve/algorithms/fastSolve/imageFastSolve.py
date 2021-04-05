import numpy as np
from PIL import Image
from cv2 import cvtColor, COLOR_RGB2GRAY
from .cvSurfDetect import sift_detect
from .imageTranslate import image_translate, validate


def image_iter_solve(ori, des, det, min_xy=None, max_xy=None,
                     min_xy1=None, max_xy1=None, loss=None):
    """
    :param ori: path of origin image
    :param des: path of destination image
    :param min_xy: feature of min xy via iterate
    :param min_xy1: feature of min xy via iterate
    :param max_xy: feature of max xy via iterate
    :param max_xy1: feature of max xy via iterate
    :param loss: loss in iterate
    :return: [[x1, y1], [x2, y2], ...[x100, y100]],[[x1, y1], [x2, y2], ...[x100, y100]], min_loss
    the first of param is point of feature, the last is minimum of loss via calculating
    """
    ori_image = Image.open(ori)
    des_image = Image.open(des)
    if min_xy is not None:
        ori_image = ori_image.crop((min_xy[0], min_xy[1], max_xy[0], max_xy[1]))
        des_image = des_image.crop((min_xy1[0], min_xy1[1], max_xy1[0], max_xy1[1]))
    ori_x, ori_y = ori_image.size
    des_x, des_y = des_image.size
    if ori_x == 0 or ori_y == 0 or des_x == 0 or des_y == 0:
        return [], [], 0
    ori_scale = 1
    des_scale = 1
    while ori_x * ori_y > 4000000 or des_x * des_y > 4000000:
        if ori_x * ori_y > 4000000:
            ori_image = ori_image.resize((int(0.5 * ori_x), int(0.5 * ori_y)))
            ori_scale = 0.5 * ori_scale
            ori_x, ori_y = int(0.5 * ori_x), int(0.5 * ori_y)
        if des_x * des_y > 4000000:
            des_image = des_image.resize((int(0.5 * des_x), int(0.5 * des_y)))
            des_scale = 0.5 * des_scale
            des_x, des_y = int(0.5 * des_x), int(0.5 * des_y)
    ori_input = cvtColor(np.asarray(ori_image), COLOR_RGB2GRAY)
    des_input = cvtColor(np.asarray(des_image), COLOR_RGB2GRAY)
    kp1, kp2, best_matches = sift_detect(ori_input, des_input, detector=det)
    ori_key = []
    des_key = []
    for i in range(len(best_matches)):
        ori_key.append(np.divide(kp1[best_matches[i][0].queryIdx].pt, [ori_scale, ori_scale]))
        des_key.append(np.divide(kp2[best_matches[i][0].trainIdx].pt, [des_scale, des_scale]))
    if len(best_matches) == 0:
        return [], [], 0
    min_xy11 = np.min(ori_key, axis=0)
    max_xy11 = np.max(ori_key, axis=0)
    min_xy111 = np.min(des_key, axis=0)
    max_xy111 = np.max(des_key, axis=0)
    print(min_xy11, max_xy11, min_xy111, max_xy111)
    a, kkk, x, y = image_translate(ori_key, des_key)
    new_loss = validate(ori_key, des_key, a, kkk, x, y)
    if loss is None:
        ori_keys, des_keys, new_loss_l = image_iter_solve(
            ori, des, det, min_xy11, max_xy11, min_xy111, max_xy111, new_loss)
        if len(ori_keys) == 0:
            return ori_key, des_key, new_loss
        ori_key_s, des_key_s = _cul_origin_point(min_xy, min_xy1, ori_keys, des_keys)
        return ori_key_s, des_key_s, new_loss_l
    elif loss > new_loss:
        ori_keys, des_keys, new_loss_l = image_iter_solve(
            ori, des, det, min_xy11, max_xy11, min_xy111, max_xy111, new_loss)
        if len(ori_keys) == 0:
            return ori_key, des_key, new_loss
        ori_key_s, des_key_s = _cul_origin_point(min_xy, min_xy1, ori_keys, des_keys)
        return ori_key_s, des_key_s, new_loss_l
    else:
        return ori_key, des_key, new_loss


def _cul_origin_point(min_xyz, min_xyz1, ori_key1, des_key1):
    if min_xyz is not None:
        return np.add(ori_key1, min_xyz), np.add(des_key1, min_xyz1)
    else:
        return ori_key1, des_key1


"""
if __name__ == '__main__':
    start_time = time.time()
    _, _, los = image_iter_solve('C:/Users/meng/Desktop/1989.jpg', 'C:/Users/meng/Desktop/19892.png')
    end_time = time.time()
    print("Loss is {} .".format(los))
    print("Time is {} s.".format(end_time-start_time))
"""