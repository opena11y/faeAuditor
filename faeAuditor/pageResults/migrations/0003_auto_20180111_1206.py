# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-11 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageResults', '0002_auto_20180110_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageguidelineresult',
            name='has_manual_checks',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pageguidelineresult',
            name='implementation_pass_fail_summ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageguidelineresult',
            name='implementation_summ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageguidelineresult',
            name='total_pages',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageresult',
            name='has_manual_checks',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pageresult',
            name='implementation_pass_fail_summ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageresult',
            name='implementation_summ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageresult',
            name='total_pages',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pagerulecategoryresult',
            name='has_manual_checks',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pagerulecategoryresult',
            name='implementation_pass_fail_summ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pagerulecategoryresult',
            name='implementation_summ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pagerulecategoryresult',
            name='total_pages',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pagerulescoperesult',
            name='has_manual_checks',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pagerulescoperesult',
            name='implementation_pass_fail_summ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pagerulescoperesult',
            name='implementation_summ',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pagerulescoperesult',
            name='total_pages',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pageruleresult',
            name='elements_hidden',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pageruleresult',
            name='elements_mc_failed',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pageruleresult',
            name='elements_mc_identified',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pageruleresult',
            name='elements_mc_na',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pageruleresult',
            name='elements_mc_passed',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pageruleresult',
            name='elements_passed',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pageruleresult',
            name='elements_violation',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pageruleresult',
            name='elements_warning',
            field=models.BigIntegerField(default=0),
        ),
    ]
