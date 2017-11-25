# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(" Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("This is about page. <br/> <a href='/rango/'>Index</a>")