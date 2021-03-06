# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-26 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditResults', '0005_auto_20181025_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditguidelineresult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditguidelineresult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditguidelineresult',
            name='implementation_summ_fail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditresult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditresult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditresult',
            name='implementation_summ_fail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditrulecategoryresult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditrulecategoryresult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditrulecategoryresult',
            name='implementation_summ_fail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditrulescoperesult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditrulescoperesult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditrulescoperesult',
            name='implementation_summ_fail',
            field=models.IntegerField(default=0),
        ),
    ]
