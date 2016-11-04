# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guideline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('num', models.IntegerField()),
                ('number', models.CharField(default=b'none', max_length=8)),
                ('url', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=32)),
            ],
            options={
                'ordering': ['principle__num', 'num'],
                'verbose_name': 'WCAG 2.0 Guideline',
                'verbose_name_plural': 'WCAG 2.0 Guidelines',
            },
        ),
        migrations.CreateModel(
            name='Principle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('num', models.IntegerField()),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['num'],
                'verbose_name': 'WCAG 2.0 Principle',
                'verbose_name_plural': 'WCAG 2.0 Principles',
            },
        ),
        migrations.CreateModel(
            name='SuccessCriterion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('level', models.CharField(choices=[(b'1', b'Level A'), (b'2', b'Level AA'), (b'3', b'Level AAA')], max_length=2)),
                ('num', models.IntegerField()),
                ('number', models.CharField(default=b'none', max_length=8)),
                ('url', models.URLField(blank=True, null=True)),
                ('url_meet', models.URLField(blank=True, null=True)),
                ('url_understand', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=32)),
                ('guideline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='success_criteria', to='wcag20.Guideline')),
            ],
            options={
                'ordering': ['guideline__principle__num', 'guideline__num', 'num'],
                'verbose_name': 'WCAG 2.0 Success Criterion',
                'verbose_name_plural': 'WCAG 2.0 Success Criteria',
            },
        ),
        migrations.AddField(
            model_name='guideline',
            name='principle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guidelines', to='wcag20.Principle'),
        ),
    ]
