# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nugget', '0004_auto_20171203_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='effect',
            field=models.IntegerField(default=5, help_text='+/- Stat1', verbose_name='+/- Stat'),
        ),
        migrations.AlterField(
            model_name='item',
            name='effect2',
            field=models.IntegerField(default=5, help_text='+/- Stat2', null=True, verbose_name='+/- Stat'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_features',
            field=models.CharField(blank=True, choices=[('he', 'Health'), ('hun', 'Hunger'), ('def', 'Defense'), ('f', 'Fatigue'), ('i', 'Intelligence'), ('happ', 'Happiness'), ('l', 'luck')], default='he', help_text='Type of Feature1', max_length=100, verbose_name='Features'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_features2',
            field=models.CharField(blank=True, choices=[('he', 'Health'), ('hun', 'Hunger'), ('def', 'Defense'), ('f', 'Fatigue'), ('i', 'Intelligence'), ('happ', 'Happiness'), ('l', 'luck')], default='he', help_text='Type of Feature2', max_length=100, null=True, verbose_name='Features'),
        ),
    ]
