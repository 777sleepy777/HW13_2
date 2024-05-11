import os
import django
from pymongo import MongoClient
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homework10.settings')
django.setup()
from quotes.models import Quotes, Tag, Author

client = MongoClient('mongodb+srv://qwerrewq:qwerrewq@mycluster.a3vheay.mongodb.net/?retryWrites=true&w=majority')

db = client.myDatabase9
authors = db.authors.find()

"""for author in authors:
    Author.objects.get_or_create(
        fullname=author["fullname"],
    born_date = author["born_date"],
    born_location = author["born_location"],
    description = author["description"]
    )"""

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        print(tag)
        t, *_ = Tag.objects.get_or_create(name = tag)
        print(t)
        tags.append(t)
    #print(quote)
    #print(quote['quote'])
    exist_quote = bool(len(Quotes.objects.filter(quote=quote['quote'])))
    if not exist_quote:
        #print(quote['author'])
        author = db.authors.find_one({'_id': quote['author']})
        #print(author["fullname"])
        a = Author.objects.get(fullname=author["fullname"])
        print(a)
        q = Quotes.objects.create(
            quote=quote["quote"],
            author = a
        )
        for tag in tags:
            q.tags.add(tag)


