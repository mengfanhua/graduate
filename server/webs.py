# -*- coding: utf-8 -*-
import os
import tornado.ioloop
import tornado.web
import platform
import json
from . import solve


settings = {
            "debug": False,
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        key = self.get_argument("key")
        key = str(key)
        self.render("upload.html", key=key)
    """
    def get(self):
        key = "default";
        self.render("upload.html", key=key)
    """

class UpdateHandler(tornado.web.RequestHandler):
    def post(self):
        z = self.get_argument("z")
        x = self.get_argument("x")
        y = self.get_argument("y")
        key = self.get_argument("key")
        # print(self.request.files.keys())
        content = self.request.files.get("img")
        # print(len(content))
        # print(content[0])
        z = str(z)
        x = str(x)
        y = str(y)
        key = str(key)
        if not os.path.exists(os.path.join("./static", key, z, x)):
            os.makedirs(os.path.join("./static", key, z, x))
        with open(os.path.join("./static", key, z, x, y + ".png"), "wb") as f:
            f.write(content[0]["body"])
            f.close()
        self.write(json.dumps(True, ensure_ascii=False))
        self.finish()


class PictureHandler(tornado.web.RequestHandler):
    def get(self):
        z = self.get_argument("z", "")
        x = self.get_argument("x", "")
        y = self.get_argument("y", "")
        key = self.get_argument("key", "")
        z = str(z)
        x = solve.exchange_to_M(str(x))
        y = solve.exchange_to_M(str(y))
        key = str(key)
        if os.path.exists(os.path.join("./static", key, z, x, y + ".png")):
            pic = open(os.path.join("./static", key, z, x, y + ".png"),'rb')
            pics=pic.read()
            self.write(pics)
            self.set_header("Content-type", "image/png")
        else:
            pic = open("./static/default.png",'rb')
            pics = pic.read()
            self.write(pics)
            self.set_header("Content-type", "image/png")
        self.finish()


class ValidateHandler(tornado.web.RequestHandler):
    def post(self):
        key = self.get_argument("key")
        z = self.get_argument("z", "")
        x = self.get_argument("x", "")
        y = self.get_argument("y", "")
        # key = self.get_argument("key", "")
        z = str(z)
        x = str(x)
        y = str(y)
        key = str(key)

        # key = str(key)
        if os.path.exists(os.path.join("./static/", key, z, x, y + ".png")):
            self.write(json.dumps(False, ensure_ascii=False))
            self.finish()
        else:
            self.write(json.dumps(True, ensure_ascii=False))
            self.finish()
 

class MapShowHandler(tornado.web.RequestHandler):
    def post(self):
        key = self.get_argument("key")
        key = str(key)
        self.render("map-show.html", key=key)
    """
    def get(self):
        key = "default"
        key = str(key)
        self.render("map-show.html", key=key)
    """



class SolveFileHandler(tornado.web.RequestHandler):
    def post(self):
        postdata = self.request.arguments
        for k in postdata:
            print(k,type(postdata[k]))
        key = self.get_argument("key")
        solve.parse_image(postdata, str(key))
        self.write(json.dumps(True, ensure_ascii=False))
        self.finish()


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        url = "upload"
        self.render("login.html", url_des=url)


class LoginShowHandler(tornado.web.RequestHandler):
    def get(self):
        url = "image-show"
        self.render("login.html", url_des=url)

def make_app():
    return tornado.web.Application([
         (r"/", MainHandler),
         (r"/pic", PictureHandler),
         (r"/update", UpdateHandler),
         (r"/validate", ValidateHandler),
         (r"/image-show", MapShowHandler),
         (r"/upload", UploadHandler),
         (r"/upload_file", SolveFileHandler),
         (r"/login_1", LoginHandler),
         (r"/login_2", LoginShowHandler),
       ], **settings)


if __name__ == "__main__":
    if platform.system() == "Windows":
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print("server startup....")
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
