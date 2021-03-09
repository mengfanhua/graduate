from PIL import Image
import os
import requests


def convertNumberToStr(value):
    if value >= 0:
        return str(value)
    else:
        return "M" + str(abs(value))


def convertStrToNumber(st):
    if st[0] == "M":
        return -int(st[1:])
    else:
        return int(st)


def combineTileToImage(start_z, start_x, start_y, len_x, len_y, cachePaths):
    """
    :param start_z: the level of image
    :param start_x: axis x on the left-up of image
    :param start_y: axis y on the left-up of image
    :param len_x: the number of image on axis x
    :param len_y: the number of image on axis y
    :param cachePaths: path of image tile
    :return: combine image (Type of Image)
    """
    image = Image.new("RGBA", (256 * len_x, 256 * len_y))
    x = start_x
    y = start_y
    m = 0
    for i in range(x, x + len_x):
        n = 0
        for j in range(y, y + len_y):
            path = os.path.join(cachePaths, str(start_z), convertNumberToStr(i), convertNumberToStr(-j) + ".png")
            if os.path.exists(path):
                tile_image = Image.open(path)
                image.paste(tile_image, (m * 256, n * 256))
            else:
                response = requests.get("https://maponline2.bdimg.com/tile/?qt=vtile&x={}&y={}&z={}&styles=pl&"
                                        "udt=20210119&scaler=1&showtext=0".format(convertNumberToStr(i),
                                                                                  convertNumberToStr(-j), start_z))
                if not os.path.exists(os.path.join(cachePaths, str(start_z), convertNumberToStr(i))):
                    os.makedirs(os.path.join(cachePaths, str(start_z), convertNumberToStr(i)))
                with open(os.path.join(path), "wb") as f:
                    f.write(response.content)
                    f.close()
                response.close()
                tile_image = Image.open(path)
                image.paste(tile_image, (m * 256, n * 256))
            n += 1
        m += 1
    return image


def divideImageToTile(image, start_z, start_x, start_y, desPaths):
    """
    :param image: combined image
    :param start_z: the level of image
    :param start_x: axis x on the left-up of image
    :param start_y: axis y on the left-up of image
    :param desPaths: destination of Image tile
    :return: None
    """
    x, y = image.size
    len_x, len_y = int(x/256), int(y/256)
    m = start_x
    for i in range(len_x):
        n = start_y
        for j in range(len_y):
            tile_image = image.crop((i * 256, j * 256, i * 256 + 256, j * 256 + 256))
            path = os.path.join(desPaths, str(start_z), convertNumberToStr(m))
            if not os.path.exists(path):
                os.makedirs(path)
            tile_image.save(os.path.join(path, convertNumberToStr(-n) + ".png"))
            n += 1
        m += 1


if __name__ == '__main__':
    # image = Image.open("C:\\Users\\meng\\Desktop\\test.png")
    # divideImageToTile(image, "3", "0", "0", "C:\\Users\\meng\\Desktop\\map")
    image = combineTileToImage("3", "0", "0", 16, 16, "C:\\Users\\meng\\Desktop\\map")
    image.save("C:\\Users\\meng\\Desktop\\test_success.png")
    # 此处函数输入需要保证输入格式为瓦片格式大小的整数倍
