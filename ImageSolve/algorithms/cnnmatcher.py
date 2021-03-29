from PIL import Image
import cv2
import numpy as np
from ImageSolve.algorithms import sobel
from ImageSolve.algorithms import features_get


def cnn_matcher(img1, img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    k1 = 800.0/min(image1.size[0], image1.size[1])
    k2 = 800.0/min(image2.size[0], image2.size[1])
    new_image1, dx1, dy1 = resize_image(image1, 800)
    new_image2, dx2, dy2 = resize_image(image2, 800)
    sobel_image1 = sobel.sobel(new_image1)
    sobel_image2 = sobel.sobel(new_image2)
    input_image1 = cv2.cvtColor(sobel_image1, cv2.COLOR_GRAY2RGB)
    input_image2 = cv2.cvtColor(sobel_image2, cv2.COLOR_GRAY2RGB)
    mask, ori_keys, des_keys = features_get.match_features_get(input_image1, input_image2)
    ori_key = []
    des_key = []
    for i in range(len(mask)):
        ori_key.append(ori_keys[mask[i][0]])
        des_key.append(des_keys[mask[i][1]])
    ori_key = np.array(ori_key, dtype=np.float32)
    des_key = np.array(des_key, dtype=np.float32)
    ori_key = ori_key/k1 + np.array([dx1, dy1])
    des_key = des_key/k2 + np.array([dx2, dy2])
    return ori_key, des_key


def resize_image(image, value):
    x, y = image.size
    if x > y:
        new_image = image.crop((int((x - y) / 2) + value, value, int((x - y) / 2) + y - value, y - value))
        xx, yy = int((x - y) / 2) + value, value
    else:
        new_image = image.crop((value, int((y - x) / 2) + value, x - value, int((y - x) / 2) + x - value))
        xx, yy = value, int((y - x) / 2) + value
    return new_image, xx, yy

