# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-17 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditResults', '0002_auto_20180809_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditguidelineresult',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='auditresult',
            name='slug',
            field=models.SlugField(blank=True, default='none', max_length=64),
        ),
        migrations.AlterField(
            model_name='auditrulecategoryresult',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='auditrulescoperesult',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=64),
        ),
    ]