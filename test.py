from PIL import Image
import cv2
import numpy as np


if __name__ == '__main__':
    path = "C:\\Users\\meng\\Desktop\\map\\3\\0\\0.png"
    image = Image.open(path)
    iamge = image.convert("L")
    asd = cv2.cvtColor(np.asarray(iamge))

