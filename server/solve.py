#encoding=utf-8
import base64
import os


def parse_image(dic, key):
    num = int(len(dic) / 2)
    for i in range(num):
        m = str(dic["data[" + str(i) + "][base64]"][0]).split(",")[-1]
        image = base64.b64decode(m)
        n = str(dic["data[" + str(i) + "][filename]"][0])[2:-1].split("/")
        if len(n)>=3:
            n = n[-3:]
        else:
            continue
        print(n)
        if not os.path.exists(os.path.join("./static/", key, n[0], n[1])):
            os.makedirs(os.path.join("./static/", key, n[0], n[1]))
        with open(os.path.join("./static/", key, n[0], n[1], n[2]), "wb") as f:
            f.write(image)
            f.close()
    return True


def exchange_to_M(x):
    if int(x) >= 0:
        return str(x)
    else:
        return "M" + str(abs(int(x)))

