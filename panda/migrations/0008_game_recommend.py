# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panda', '0007_auto_20180322_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='recommend',
            field=models.ManyToManyField(blank=True, related_name='_game_recommend_+', to='panda.Game'),
        ),
    ]