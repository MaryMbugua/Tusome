# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vitabu',
            name='ifuku_image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
