# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-28 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panda', '0002_game_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='gamerating',
            old_name='user',
            new_name='player',
        ),
        migrations.AddField(
            model_name='player',
            name='rating',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='playerrating',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='panda.Player'),
        ),
        migrations.AddField(
            model_name='playerrating',
            name='rated_player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_player', to='panda.Player'),
        ),
    ]
