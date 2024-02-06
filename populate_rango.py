import os
import random
import django
import django.apps
from django.urls import reverse, reverse_lazy


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

django.setup()
from rango.models import Category, Page


def populate():

    python_pages = [
       {'title': 'Official Python Tutorial',
       'url':'http://docs.python.org/3/tutorial/'},
       {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/'} ]
    
    other_pages = [
       {'title':'Bottle',
       'url':'http://bottlepy.org/docs/dev/'},
       {'title':'Flask',
        'url':'http://flask.pocoo.org'} ]
    
    django_pages = [
        {'title':'Official Django Tutorial',
    'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
    {'title':'Django Rocks',
    'url':'http://www.djangorocks.com/'},
    {'title':'How to Tango with Django',
    'url':'http://www.tangowithdjango.com/'} ]

    #changed from origional code, there are now views and likes in this dictionary
    cats = {
        'Python': {
            'pages': python_pages,
            'views': 128,
            'likes': 64
        },
        'Django': {
            'pages': django_pages,
            'views': 64,
            'likes': 32
        },
        'Other Frameworks': {
            'pages': other_pages,
            'views': 32,
            'likes': 16
        }
    }
    for name, cat in cats.items():
        c = Category.objects.filter(name=name).first()
        if not c:  # Only add the category if it doesn't already exist
            c = add_cat(name, views=cat['views'], likes=cat['likes'])
        for p in cat['pages']:
            views = random.randint(1, 100) 
            add_page(c, p['title'], p['url'], views=views)
        c.save()

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')
def add_page(cat, title, url, views=0):
    p, created = Page.objects.get_or_create(category=cat, title=title)
    if created:  # Only set the url and views if the page was just created
        p.url = url
        p.views = views
        p.save()
    return p

def add_cat(name, views=0, likes=0):
    c, created = Category.objects.get_or_create(name=name)
    if created:
        c.views = views
        c.likes = likes
        c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()