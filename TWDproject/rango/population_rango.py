import os
os.environ.setdefault('DJANGO_SETTING_MODUEL', 'TWDproject.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    
    # Category 'Python'
    python_cat = add_cat('Python')
    
    add_page(
        category=python_cat,
        title='How to think like a computer science'
        url='http://docs.python.org/2/tutorial/')
        
    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    # Categoty 'Django'
    django_cat = add_cat("Django")

    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    # Category Frameworks
    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")

    for c in Category.objects.all():
        for p in Page.objects.all():
            print "- {0} - {1}".format(str(c), str(p))


def add_cat(name):
    c = Category.objects.get_or_create (name=name)
    return c


def add_page(category, title, url, views=0):
    p = Page.objects.get_or_create(category=category, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p 


# Start execution
if __name__ = '__main__':
    print 'Starting Rango population script...'
    populate()

