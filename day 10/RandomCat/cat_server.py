import random
import tornado.ioloop
import tornado.web
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://user:password@ds129352.mlab.com:29352/goto_summer_cats")
database = client["goto_summer_cats"]
cats_collection = database["cats"]


class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('add.html')
    def post(self):
        name = self.get_argument("name")
        photo = self.get_argument("photo")

        cat = {"name": name, "photo": photo, "likes": 0, "comments": []}
        cats_collection.insert(cat)
        self.redirect('/?id='+str(cat['_id']))

class LikeHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument('id', '')
        if id != '':
            cat = cats_collection.find_one({'_id': ObjectId(id)})
            cat["likes"] += 1
            cats_collection.update({'_id': ObjectId(id)}, cat)
        self.redirect('/?id='+id)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument('id', '')
        if id != '':
            cat = cats_collection.find_one({'_id': ObjectId(id)})
        else:
            cats = list(cats_collection.find())
            cat = random.choice(cats)
        self.render("cat.html", cat=cat)
    def post(self):
        id = self.get_argument('id', '')
        text = self.get_argument('text', '')
        email = self.get_argument('email', '')

        cat = cats_collection.find_one({'_id': ObjectId(id)})
        cat['comments'].append({"email": email, "text": text})
        cats_collection.update({'_id': ObjectId(id)}, cat)

        self.redirect('/?id=' + id)



routes = [
    (r"/", MainHandler),
    (r"/like", LikeHandler),
    (r"/add", AddHandler)
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()
