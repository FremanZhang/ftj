# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    # return HttpResponse(" Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
    context_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'top5_categories': context_list}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {
        'aboutmessage': 'Welcome for contact as below.'
    }
    return render(request, 'rango/about.html', context_dict)
    # return HttpResponse("This is about page. <br/> <a href='/rango/'>Index</a>")


def category(request, category_name_slug):
    context_dict = {}
    try:
        c = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = c.name 
        
        pages = Page.objects.filter(category=c)
        context_dict['pages'] = pages
        context_dict['category'] = c
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)

