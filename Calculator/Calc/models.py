# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.

class Calculations (models.Model):
     calc1 = models.CharField(max_length=15)
     calc2 = models.CharField(max_length=15)
     result = models.CharField(max_length=15)
     

     def __str__(self):
       return self.calc1 + '+' + self.calc2 + '='+self.result
    


     

