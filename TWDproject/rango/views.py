# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
# from django.http import Http404
# from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    # return HttpResponse(" Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
    context_list_category = Category.objects.order_by('-likes')[:5]
    content_list_page = Page.objects.order_by('-views')[:5]
    context_dict = {'top5_categories': context_list_category, 'top5_pages': content_list_page}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {
        'aboutmessage': 'Welcome for contact as below.'
    }
    return render(request, 'rango/about.html', context_dict)
    # return HttpResponse("This is about page. <br/> <a href='/rango/'>Index</a>")


def category(request, category_name_slug):
    context_dict = {}
    # try:
    #     c = Category.objects.get(slug=category_name_slug)
    #     context_dict['category_name'] = c.name 
        
    #     pages = Page.objects.filter(category=c)
    #     context_dict['pages'] = pages
    #     context_dict['category'] = c
    # except Category.DoesNotExist:
    #     raise Http404('Category does not exist.')

    c = get_object_or_404(Category, slug=category_name_slug)
    context_dict['category_name'] = c.name 
    
    pages = Page.objects.filter(category=c)
    context_dict['pages'] = pages
    context_dict['category'] = c


    return render(request, 'rango/category.html', context_dict)

