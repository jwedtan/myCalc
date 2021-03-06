# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-27 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calc1', models.CharField(max_length=15)),
                ('calc2', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_text', models.CharField(max_length=15)),
                ('result', models.IntegerField(default=0)),
                ('operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Calc.Calculations')),
            ],
        ),
    ]
