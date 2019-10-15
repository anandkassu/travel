# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Destination
from .models import ExpenseAccount
from .models import ExpenseItem
from .models import ExpenseCategory
from .models import Message


# Register your models here.
admin.site.register(Destination)



admin.site.register(ExpenseAccount)

admin.site.register(ExpenseItem)

admin.site.register(ExpenseCategory)

admin.site.register(Message)
