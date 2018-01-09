# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
'''
# Preceding register
admin.site.register(Category)
admin.site.register(Page)
'''


# Admin regisyer decorator
@admin.register(Category,Page)

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'views', 'likes')
    empty_value_display = '-'
    

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')
    empty_value_display = '-'
