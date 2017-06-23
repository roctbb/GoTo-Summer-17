from pymongo import MongoClient

client = MongoClient("mongodb://user:password@ds129352.mlab.com:29352/goto_summer_cats")
database = client["goto_summer_cats"]
cats_collection = database["cats"]

cats_collection.remove()

'''
cats_collection.insert({....}) - добавление документа
cats_collection.find() - все документы в базе
cats_collection.find({"name": "Барсик"}) - все Барсики
cats_collection.remove({"name": "Барсик"}) - удалить всех Барсиков
cats_collection.update({"name": "Барсик"}, {"name": "Васька"})
'''

cats = [
    {"name": "Хахатонщик", "comments": [], "likes": 0, "photo": "https://xn--e1afgbgom0e.xn--p1ai/upload/iblock/4d4/1446136120_funny_omg_cat_ob.jpg"},
    {"name": "Кубышка", "comments": [], "likes": 0, "photo": "http://cs8.pikabu.ru/post_img/2016/03/08/0/1457386499120176766.jpg"},
    {"name": "Бывалый", "comments": [], "likes": 0, "photo": "http://lady.izvestia.kiev.ua/images/2015-05/27/1hWlIVaERSt8uvft/img_top.jpg"},
    {"name": "Горбун", "comments": [], "likes": 0, "photo": "http://hitgid.com/images/%D0%BA%D0%BE%D1%82-6.jpg"},
]

cats_collection.insert(cats)