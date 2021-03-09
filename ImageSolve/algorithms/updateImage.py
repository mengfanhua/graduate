import requests
from ImageSolve.algorithms.generateKey import generate_key


def update_image(path, z, x, y, key):
    try:
        files = {'img': open(path, 'rb')}
        datas = {"x": x, "y": y, "z": z, "key": key}
        with open("./Resources/host", "r", encoding="utf-8") as f:
            host = f.read()
            f.close()
        response = requests.post(host + "/update", data=datas, files=files)
        data = response.text
        response.close()
        print(data)
        if data == "true":
            return True
        else:
            return False
    except:
        return False


def validate_key(z, x, y, key):
    try:
        datas = {"x": x, "y": y, "z": z, "key": key}
        with open("./Resources/host", "r", encoding="utf-8") as f:
            host = f.read()
            f.close()
        response = requests.post(host + "/validate", data=datas)
        data = response.text
        response.close()
        if data == "true":
            return True
        else:
            return False
    except:
        return False


if __name__ == '__main__':
    path = "C:\\Users\\meng\\Desktop\\map\\3\\0\\0.png"
    z = "3"
    x = "0"
    y = "0"
    key = generate_key("mengfanhua", "mengfanhua")
    print(update_image(path, z, x, y, key))
