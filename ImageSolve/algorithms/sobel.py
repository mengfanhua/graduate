import numpy as np
from PIL import Image


def sobel(img):
    #img = Image.open(path)
    image = img.resize((800, 800), Image.ANTIALIAS)
    img = image.convert("L")
    # 先放缩加快处理速度，然后转换成灰度图像
    img_array = np.array(img, dtype=np.float64)
    x, y = img_array.shape
    gx = sobel_H(img_array, x, y)
    # 横向sobel算子
    gy = sobel_V(img_array, x, y)
    # 纵向sobel算子
    g = np.sqrt(np.multiply(gx, gx)+np.multiply(gy, gy))
    # g = sqrt(x*x+y+y)
    grid = np.arctan(np.divide(gy, gx))
    # grid 为各像素点的梯度
    # g = g.reshape((1, x*y))
    #grid = grid.reshape((1, x*y))
    g = 255 - g
    # im = Image.fromarray(g.astype('uint8'))
    return g.astype('uint8')


def sobel_H(img, x, y):
    xx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    xxx = np.array(xx)
    gx = np.zeros((x, y))
    for i in range(1, x - 1):
        for j in range(1, y - 1):
            # 按照卷积方法构造新的点
            gx[i][j] = np.sum(np.multiply(xxx, img[i - 1:i + 2, j - 1:j + 2]))
    return gx.copy()


def sobel_V(img, x, y):
    yy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    yyy = np.array(yy)
    gy = np.zeros((x, y))
    for i in range(1, x - 1):
        for j in range(1, y - 1):
            # 按照卷积方法构造新的点
            gy[i][j] = np.sum(np.multiply(yyy, img[i - 1:i + 2, j - 1:j + 2]))
    return gy.copy()


"""
if __name__ == '__main__':
    img1 = Image.open("C:/Users/meng.fh/Desktop/19891.jpg")
    _, _, img2 = sobel(img1)
    img3 = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
    cv2.imshow("title", img3)
    cv2.waitKey()
"""