import random

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cats = [
            {"name": "Хахатонщик", "photo": "https://xn--e1afgbgom0e.xn--p1ai/upload/iblock/4d4/1446136120_funny_omg_cat_ob.jpg"},
            {"name": "Кубышка", "photo": "http://cs8.pikabu.ru/post_img/2016/03/08/0/1457386499120176766.jpg"},
            {"name": "Бывалый", "photo": "http://lady.izvestia.kiev.ua/images/2015-05/27/1hWlIVaERSt8uvft/img_top.jpg"},
            {"name": "Горбун", "photo": "http://hitgid.com/images/%D0%BA%D0%BE%D1%82-6.jpg"},
        ]

        cat = random.choice(cats)
        self.render("cat.html", name=cat["name"], image=cat["photo"])

routes = [
        (r"/", MainHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()