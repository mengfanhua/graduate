import json


proxy = {}


def proxyInit():
    try:
        f = open("./Resources/proxy", "r", encoding="utf-8")
        pro = json.loads(f.read())
        f.close()
        for i in pro:
            proxy[i] = pro[i]
    except:
        pass


def proxyChange(newProxy):
    proxy.clear()
    for i in newProxy:
        proxy[i] = newProxy[i]
    with open("./Resources/proxy", "w", encoding="utf-8") as f:
        f.write(json.dumps(newProxy))
        f.close()
