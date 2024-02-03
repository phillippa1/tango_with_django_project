import os
import random
from rango.models import Category, Page
from django.urls import reverse, reverse_lazy


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
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
        c = add_cat(name, views=cat['views'], likes=cat['likes'])
        for p in cat['pages']:
            add_page(c, p['title'], p['url'])
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


# Python = add_cat('Python', cats['Python']['views'],cats['Python']['likes'])
    # add_page(Python, 'Official Python Tutorial', reverse('rango:tutorial'))
    # add_page(Python, 'Django Rocks', 'http://docs.python.org/3/tutorial/')
    # add_page(Python, 'How to Tango with Django', 'http://docs.python.org/3/tutorial/')

    # Django = add_cat('Django', cats['Django']['views'],cats['Django']['likes'])
    # add_page(Django, 'Official Django Tutorial', reverse('rango:tutorial'))
    # add_page(Django, 'Django Rocks', 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/')
    # add_page(Django, 'How to Tango with Djang', 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/')

    # Other = add_cat('Other Frameworks', cats['Other Frameworks']['views'],cats['Other Frameworks']['likes'])
    # add_page(Other, 'Official Django Tutorial', reverse('rango:tutorial'))
    # add_page(Other, 'Django Rocks', 'http://bottlepy.org/docs/dev/')
    # add_page(Other, 'How to Tango with Django', 'http://bottlepy.org/docs/dev/')

    #for cat, cat_data in cats.items():
    #     c = add_cat(cat, cat_data['views'], cat_data['likes'])
    #     for p in cat_data['pages']:
    #         add_page(c, p['title'], p['url'], cat_data['views'])
    #     c.save() 

    # for c in Category.objects.all():
    #     for p in c.pages.all():
    #         add_page(c, p['title'], p['url'], c.views, c.likes)

