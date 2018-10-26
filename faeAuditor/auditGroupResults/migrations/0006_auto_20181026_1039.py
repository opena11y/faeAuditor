# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-26 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditGroupResults', '0005_auto_20181025_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditgroupguidelineresult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgroupguidelineresult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgroupguidelineresult',
            name='implementation_summ_fail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditgroupresult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgroupresult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgroupresult',
            name='implementation_summ_fail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditgrouprulecategoryresult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgrouprulecategoryresult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgrouprulecategoryresult',
            name='implementation_summ_fail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auditgroupruleresult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgroupruleresult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgrouprulescoperesult',
            name='implementation_score_fail',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgrouprulescoperesult',
            name='implementation_score_mc',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=4),
        ),
        migrations.AddField(
            model_name='auditgrouprulescoperesult',
            name='implementation_summ_fail',
            field=models.IntegerField(default=0),
        ),
    ]
