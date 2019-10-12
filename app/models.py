# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Destination(models.Model):
    
    img= models.ImageField(upload_to='pics')
    price= models.IntegerField()
    name = models.TextField()
    des = models.CharField( max_length=250)
    offer= models.BooleanField(default=False)
