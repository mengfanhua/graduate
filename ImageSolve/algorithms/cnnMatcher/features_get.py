import cv2
import numpy as np
from .libAlg.cnn_feature import cnn_feature_extract
import time
from skimage import measure
from skimage import transform


def match_features_get(image1,image2):

    _RESIDUAL_THRESHOLD = 20

    # read left image
    # image1 = imageio.imread(imgfile1)
    # image2 = imageio.imread(imgfile2)

    start0 = time.perf_counter()

    kps_left, sco_left, des_left = cnn_feature_extract(image1,  nfeatures = -1)
    kps_right, sco_right, des_right = cnn_feature_extract(image2,  nfeatures = -1)

    print('Feature_extract time is %6.3f, left: %6.3f,right %6.3f' % ((time.perf_counter() - start0), len(kps_left), len(kps_right)))
    start = time.perf_counter()

    # Flann特征匹配
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=40)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des_left, des_right, k=2)

    goodMatch = []
    locations_1_to_use = []
    locations_2_to_use = []

    # 匹配对筛选
    min_dist = 1000
    max_dist = 0
    disdif_avg = 0
    # 统计平均距离差
    for m, n in matches:
        disdif_avg += n.distance - m.distance
    disdif_avg = disdif_avg / len(matches)

    for m, n in matches:
        # 自适应阈值
        if n.distance > m.distance + disdif_avg:
            goodMatch.append(m)
            p2 = cv2.KeyPoint(kps_right[m.trainIdx][0],  kps_right[m.trainIdx][1],  1)
            p1 = cv2.KeyPoint(kps_left[m.queryIdx][0], kps_left[m.queryIdx][1], 1)
            locations_1_to_use.append([p1.pt[0], p1.pt[1]])
            locations_2_to_use.append([p2.pt[0], p2.pt[1]])

    # goodMatch = sorted(goodMatch, key=lambda x: x.distance)
    print('match num is %d' % len(goodMatch))
    locations_1_to_use = np.array(locations_1_to_use)
    locations_2_to_use = np.array(locations_2_to_use)

    inliers = None
    for i in range(20):
        _, inlierss = measure.ransac((locations_1_to_use, locations_2_to_use),
                                    transform.AffineTransform,
                                    min_samples=3,
                                    residual_threshold=_RESIDUAL_THRESHOLD,
                                    max_trials=2000)
        print('Found %d inliers' % sum(inlierss))
        if inliers is None:
            inliers = np.array(inlierss, dtype=np.int8)
        else:
            inliers += np.array(inlierss, dtype=np.int8)

    max_count = max(inliers)
    min_count = min(inliers)
    avg_count = int((max_count+min_count)/2)
    inliers = np.minimum(np.maximum(inliers-avg_count, 0), 1)
    inliers = np.array(inliers, dtype=np.bool8)
    inlier_idxs = np.nonzero(inliers)[0]
    # 最终匹配结果
    print(inlier_idxs)
    matches = np.column_stack((inlier_idxs, inlier_idxs))
    print('whole time is %6.3f' % (time.perf_counter() - start0))
    print("最终匹配点的数量：" + str(matches.shape[0]))
    # sar_x_y = []
    # optical_x_y = []
    #
    # sar_x_y_sec = []
    # optical_x_y_sec = []
    #
    # # sar图像和光学图像最终的匹配点对
    # for i in range(int(matches.shape[0] / 2)):
    #     idx1 = matches[i, 0]
    #     idx2 = matches[i, 1]
    #     # sar图像匹配点的列坐标和行坐标
    #     sar_x_y.append([locations_1_to_use[idx1,0],locations_1_to_use[idx1,1]])
    #     # 光学图像匹配点的列坐标和行坐标
    #     optical_x_y.append([locations_2_to_use[idx2,0],locations_2_to_use[idx2,1]])
    #
    #     if (locations_2_to_use[idx2,0] >= locations_1_to_use[idx1,0] and locations_2_to_use[idx2,1] >= locations_1_to_use[idx1,1]):
    #         sar_x_y_sec.append([locations_1_to_use[idx1,0],locations_1_to_use[idx1,1]])
    #         optical_x_y_sec.append([locations_2_to_use[idx2,0],locations_2_to_use[idx2,1]])
    #
    # optical_x_y = np.array(optical_x_y)
    # sar_x_y = np.array(sar_x_y)
    #
    # optical_x_y_sec = np.array(optical_x_y_sec)
    # sar_x_y_sec = np.array(sar_x_y_sec)
    #
    # # 求sar和光学图像匹配的特征点的列坐标和行坐标的均值，并进行四舍五入取整
    # optical_x_y_mean = np.around(optical_x_y.mean(axis=0))
    # sar_x_y_mean = np.around(sar_x_y.mean(axis=0))
    #
    # # 备用
    # if optical_x_y_sec.shape[0] == 0:
    #     optical_x_y_sec_mean = np.array([0,0])
    #     sar_x_y_sec_mean = np.array([0,0])
    # else:
    #     optical_x_y_sec_mean = np.around(optical_x_y_sec.mean(axis=0))
    #     sar_x_y_sec_mean = np.around(sar_x_y_sec.mean(axis=0))
    #
    # print("***********均值坐标*************")
    # print(optical_x_y_mean)
    # print(sar_x_y_mean)
    #
    # # 求出sar图像在光学图像中的左上角坐标
    # res_x = int(optical_x_y_mean[0] - sar_x_y_mean[0])
    # res_y = int(optical_x_y_mean[1] - sar_x_y_mean[1])
    #
    # if res_x <= 0 or res_y <= 0:
    #     res_x = int(optical_x_y_sec_mean[0] - sar_x_y_sec_mean[0])
    #     res_y = int(optical_x_y_sec_mean[1] - sar_x_y_sec_mean[1])
    #
    # print("**************sar图像在光学图像上的左上角坐标****************")
    # print(res_x,res_y)
    return matches, locations_1_to_use, locations_2_to_use
