import requests
import threading
import time
import os
import random
import json
import sys
import inspect
import ctypes
import math


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


# 打印输出到log.txt
class Logger(object):
    def __init__(self, filename="log.txt"):
        self.terminal = sys.stdout
        self.log = open(filename, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger()

exit = 1
osLock = threading.Lock()
osLock1 = threading.Lock()
getLock = threading.Lock()


# res = requests.get("https://maponline2.bdimg.com/tile/?qt=vtile&x=0&y=0&z=1&styles=pl&udt=20210119&scaler=1&showtext=0")
class myThread(threading.Thread):
    def __init__(self, threadID, name, flag_x, flag_y, path):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.x = flag_x
        self.y = flag_y
        self.path = path

    def run(self):
        print("开启线程： " + self.name)
        try:
            # 获取锁，用于线程同步
            for i in range(3, 6):
                maxs = math.ceil(math.pi * 6378137 / math.pow(2, 26 - i))
                osLock.acquire()
                if not os.path.exists(os.path.join(self.path, str(i))):
                    os.mkdir(os.path.join(self.path, str(i)))
                osLock.release()
                j = 0
                if self.x == -1:
                    j += 1
                while j <= maxs:
                    k = 0
                    if self.x == -1:
                        xx = "M" + str(j)
                    else:
                        xx = str(j)
                    osLock1.acquire()
                    if not os.path.exists(os.path.join(self.path, str(i), str(xx))):
                        os.mkdir(os.path.join(self.path, str(i), str(xx)))
                    osLock1.release()
                    if self.y == -1:
                        k += 1
                    while k <= maxs:
                        if self.y == -1:
                            yy = "M" + str(k)
                        else:
                            yy = str(k)
                        # getLock.acquire()
                        time.sleep(random.randint(1, 10))
                        flag = get_one_map(xx, yy, str(i), self.path)
                        # getLock.release()
                        if flag is True:
                            k += 1
                        else:
                            break
                    print("x={} & y=0-{} & z={} 已获取完成。".format(xx, yy, i))
                    if (k == 0 and self.y == 1) or (k == 1 and self.y == -1):
                        break
                    else:
                        j += 1
            print("关闭线程： " + self.name)
        except Exception as e:
            global exit
            exit = 0
            print(e)
            print("异常线程： " + self.name)


def get_one_map(x, y, z, path):
    print("x={} & y={} & z={}".format(x, y, z))
    try:
        res = requests.get(
            "https://maponline2.bdimg.com/tile/?qt=vtile&x={}&y={}&z={}&styles=pl&udt=20210119&scaler=1&showtext=0".format(
                x, y, z))
        data = res.content
        res.close()
        if len(data) > 197:
            with open(os.path.join(path, z, x, y) + ".png", "wb") as f:
                f.write(data)
                f.close()
            return True
        return False
    except:
        print("x={} & y={} & z={} error.".format(x, y, z))
        return True


threads = []
path = os.path.join("E:\\", "map")
print(path)
thread1 = myThread(1, "Thread-1", 1, 1, path)
thread2 = myThread(2, "Thread-2", 1, -1, path)
thread3 = myThread(3, "Thread-3", -1, 1, path)
thread4 = myThread(4, "Thread-4", -1, -1, path)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)

for t in threads:
    if exit == 1:
        t.join()
    else:
        stop_thread(t)

print("主线程退出。")