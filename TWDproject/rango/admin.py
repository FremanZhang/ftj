# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'views', 'likes')
    empty_value_display = '-'
    

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')
    empty_value_display = '-'

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
