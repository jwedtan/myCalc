# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms


# Create your models here.

class Calculations (models.Model):
     calc1 = models.CharField(max_length=15)
     calc2 = models.CharField(max_length=15)
     

     def __str__(self):
        return Calculations.objects.all()
     
class Result (models.Model):
    operation = models.ForeignKey(Calculations, on_delete=models.CASCADE)
    result_text = models.CharField(max_length=15)
    result = models.IntegerField(default=0)

    def __str__(self):
        return self.result_text
     