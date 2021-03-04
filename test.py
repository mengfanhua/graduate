from ImageSolve.algorithms.generateKey import generate_key
from ImageSolve.algorithms.updateImage import update_image


if __name__ == '__main__':
    path = "C:\\Users\\meng\\Desktop\\map\\3\\0\\0.png"
    z = "3"
    x = "0"
    y = "0"
    key = generate_key("mengfanhua", "mengfanhua")
    print(update_image(path, z, x, y, key))
