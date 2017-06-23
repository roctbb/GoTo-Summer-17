import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h3>Hello, world</h3>")
        self.write("<p>Это очень интересный веб сайт, я отвечаю!</p>")
        self.write("<img src='https://s.tcdn.co/eb3/785/eb3785af-ebcb-331c-9928-c9fb7f2fc260/192/1.png' />")
        self.write("<a href='/money'>Предложение для вас!</a>")

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "уважаемый")
        self.write("<h3>Уникальное предложение!</h3>")
        self.write("<p>Здpaвствуйте, {name}. "
                   "Пpедcтавьтe себe сuтyaцию: вы пpоснулиcь и обнaружuлu, что вce дeньгu, которыe у Вас были, иcчезлu. Полноcтью u безвозвpатно. "
                   "Сгорелu счеmа, нaкопления нa карте. "
                   "Счuтaeте выхода большe нeт? Отнюдь, выход ecть всeгда!</p>".format(name=name))

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("form.html")


routes = [
        (r"/", MainHandler),
        (r"/hello", HelloHandler),
        (r"/money", FormHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()