# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrumuser',
            name='denorm_score',
            field=models.IntegerField(default=0),
        ),
    ]