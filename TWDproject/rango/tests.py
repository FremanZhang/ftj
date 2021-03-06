# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rango.models import Category

# Create your tests here.
class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views>=0), True)


    def test_slug_line_creation(self):
        cat = Category('random category string')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')