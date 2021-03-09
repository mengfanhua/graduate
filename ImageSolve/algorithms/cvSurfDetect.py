from imagedt.decorator import time_cost
import cv2
import time
import json
from ImageSolve.algorithms.imageTranslate import image_translate, validate

# print('cv version: ', cv2.__version__)


def bgr_rgb(im):
    (r, g, b) = cv2.split(im)
    return cv2.merge([b, g, r])


def orb_detect(image_aa, image_bb):
    # feature match
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(image_aa, None)
    kp2, des2 = orb.detectAndCompute(image_bb, None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1, des2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
    # Draw first 10 matches.
    img3 = cv2.drawMatches(image_aa, kp1, image_bb, kp2, matches, None, flags=2)
    return bgr_rgb(img3)


@time_cost
def sift_detect(img1, img2, detector='surf'):
    if detector.startswith('si'):
        print("sift detector......")
        sift = cv2.xfeatures2d.SIFT_create()
    else:
        print("surf detector......")
        sift = cv2.xfeatures2d.SURF_create()
    # find the key points and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # get point from key points
    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    # Apply ratio test
    good = [[m] for m, n in matches if m.distance < 0.7 * n.distance]
    matches = sorted(good, key=lambda x: x[0].distance)
    """
    with open("./feature.txt", "w") as f:
        for i in range(len(matches)):
            f.write(json.dumps([matches[i][0].distance, kp1[matches[i][0].queryIdx].pt,
                                kp2[matches[i][0].trainIdx].pt, matches[i][0].imgIdx]))
            f.write("\n")
            f.close()
    # cv2.drawMatchesKnn expects list of lists as matches.
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches[:100], None, flags=2)
    return bgr_rgb(img3)
    """
    if len(matches) >= 100:
        return kp1, kp2, matches[:100]
    else:
        return kp1, kp2, matches


if __name__ == "__main__":
    # load image
    start_time = time.time()
    image_a = cv2.imread('C:/Users/meng/Desktop/1989.jpg')  # 绝对路径
    image_b = cv2.imread('C:/Users/meng/Desktop/19892.png')
    """
    # ORB
    # img = orb_detect(image_a, image_b)
    # SIFT or SURF
    img = sift_detect(image_a, image_b, detector="surf")
    end_time = time.time()
    print("time is {} s.".format(end_time-start_time))
    # plt.imshow(img)
    # plt.show()
    """
    kp1, kp2, best_matches = sift_detect(image_a, image_b, detector="surf")
    ori_key = []
    des_key = []
    for i in range(len(best_matches)):
        ori_key.append(kp1[best_matches[i][0].queryIdx].pt)
        des_key.append(kp2[best_matches[i][0].trainIdx].pt)
    a, kkk, x, y = image_translate(ori_key, des_key)
    new_loss = validate(ori_key, des_key, a, kkk, x, y)
    end_time = time.time()
    print("Loss is {} .".format(new_loss))
    print("Time is {} s.".format(end_time - start_time))
