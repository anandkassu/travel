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

    #create table in postgres database 
    # to see table info run command 
    #python manage.py sqlmigrate <app_name> <migration_file_name>


## models for budgets

class ExpenseAccount(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', blank=True, null=True)
    balance = models.IntegerField('Balance', default=0)

    def __str__(self):
        return self.title


class ExpenseCategory(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'ExpenseCategories'


class ExpenseItem(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', blank=True, null=True)
    account = models.ForeignKey(ExpenseAccount, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField('Date', max_length=200)
    amount = models.IntegerField('Balance')
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    title = models.CharField('Title', max_length=100)
    email = models.CharField('Email', max_length=20)
    message = models.TextField('Message', blank=True, null=True)

    def __str__(self):
        return self.title
