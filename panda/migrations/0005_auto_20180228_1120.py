# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-28 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panda', '0004_auto_20180228_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(blank=True, to='panda.Player'),
        ),
    ]