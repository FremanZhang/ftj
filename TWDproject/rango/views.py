# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse(" Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
    context_dict = {'boldmessage': 'I am bold front from the context.'}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {
        'aboutmessage': 'Welcome for contact as below.'
    }
    return render(request, 'rango/about.html', context_dict)
    # return HttpResponse("This is about page. <br/> <a href='/rango/'>Index</a>")