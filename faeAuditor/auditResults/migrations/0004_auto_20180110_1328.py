# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-10 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditResults', '0003_auto_20180107_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditruleresult',
            name='elements_hidden',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='elements_mc_failed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='elements_mc_identified',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='elements_mc_na',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='elements_mc_passed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='elements_passed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='elements_violation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='elements_warning',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='rule_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='auditruleresult',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=32),
        ),
    ]
