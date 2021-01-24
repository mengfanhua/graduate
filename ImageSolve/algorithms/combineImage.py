from PIL import Image
import math
# from ImageSolve.algorithms.imageFastSolve import image_iter_solve
# from ImageSolve.algorithms.imageTranslate import image_translate


def combine_image(front_image_path, back_image_path, k, alpha, dx, dy):
    """
    :param front_image_path: path of front image
    :param back_image_path: path of background image
    :param k: scale
    :param alpha: angle of rotate
    :param dx: offset of x
    :param dy: offset of y
    :return: combined image and origin point of background image on new image
    """
    front_image = Image.open(front_image_path)
    back_image = Image.open(back_image_path)
    front = front_image.convert("RGBA")
    back = back_image.convert("RGBA")
    f_x, f_y = front.size
    front = front.resize((int(f_x*k), int(f_y*k)), Image.ANTIALIAS)  # 此处放缩尽可能放大，否则会损失精度，必要时可放大背景图
    front = front.rotate(-alpha, expand=True)
    nf_x, nf_y = front.size
    b_x, b_y = back.size
    off_x = k * math.cos(math.radians(alpha)) * f_x / 2 - k * math.sin(math.radians(alpha)) * f_y / 2 - nf_x / 2
    off_y = k * math.sin(math.radians(alpha)) * f_x / 2 + k * math.cos(math.radians(alpha)) * f_y / 2 - nf_y / 2
    min_x = min((-off_x + dx), 0)
    min_y = min((-off_y + dy), 0)
    max_x = max((nf_x + off_x - dx), b_x)
    max_y = max((nf_y + off_y - dy), b_y)
    bottom_image = Image.new("RGBA", (int(max_x - min_x), int(max_y-min_y)))
    bottom_image.paste(back, (int(-min_x), int(-min_y)), back)
    bottom_image.paste(front, (int(-min_x - off_x + dx), int(-min_y - off_y + dy)), front)
    return bottom_image, [int(-min_x), int(-min_y)]


"""
if __name__ == '__main__':
    ori_key, des_key, _ = image_iter_solve('C:/Users/meng/Desktop/19892.png',
                                           'C:/Users/meng/Desktop/1989.jpg')
    alpha, k, dx, dy = image_translate(ori_key, des_key)
    print(alpha, k, dx, dy)
    a, _ = combine_image('C:/Users/meng/Desktop/19892.png',
                         'C:/Users/meng/Desktop/1989.jpg', k, alpha, dx, dy)
"""
