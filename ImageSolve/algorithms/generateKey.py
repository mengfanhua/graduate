import hashlib


def generate_key(username, password):
    MD5 = hashlib.md5()
    link = str(username) + str(password)
    MD5.update(link.encode("utf-8"))
    return MD5.hexdigest()


if __name__ == '__main__':
    print(generate_key(123456, "asdfghlg"))
