# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Model
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField(max_length=256)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User) #create a model with a one-to-one association with the the `User` model
    website = models.URLField(max_length=256, blank=True)
    
    #Does it create 'MEDIA_ROOT/profile_images/'? YES
    picture = models.ImageField(blank=True, upload_to='profile_images') 

    def __unicode__(self):
        return self.user.username

