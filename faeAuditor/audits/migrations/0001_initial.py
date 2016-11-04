# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 16:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rulesets', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True)),
                ('title', models.CharField(max_length=512, verbose_name=b'Audit Title')),
                ('depth', models.IntegerField(choices=[(1, b'Start URL only'), (2, b'First level links'), (3, b'Second level links')], default=2)),
                ('max_pages', models.IntegerField(choices=[(5, b'   5 pages'), (10, b'  10 pages'), (25, b'  25 pages'), (50, b'  50 pages'), (100, b' 100 pages'), (200, b' 200 pages'), (400, b' 400 pages'), (800, b' 800 pages')], default=0, verbose_name=b'Maximum Pages')),
                ('wait_time', models.IntegerField(choices=[(30000, b' 30 seconds'), (45000, b' 45 seconds'), (60000, b' 60 seconds'), (90000, b' 90 seconds'), (120000, b'120 seconds')], default=30000)),
                ('browser_emulation', models.CharField(choices=[(b'Firefox', b'Mozilla Firefox'), (b'IE', b'Microsoft Internet Explorer'), (b'Chrome', b'Google Chrome')], default=b'Chrome', max_length=32, verbose_name=b'Browser Emulation')),
                ('follow', models.IntegerField(choices=[(1, b'Specified domain only'), (2, b'Next-level subdomains')], default=1, verbose_name=b'Follow Links in')),
                ('ruleset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rulesets.Ruleset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Audit',
                'verbose_name_plural': 'Audits',
            },
        ),
        migrations.CreateModel(
            name='AuditGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True)),
                ('title', models.CharField(default=b'no group title', max_length=512, verbose_name=b'Group Title')),
                ('position', models.IntegerField(default=0, verbose_name=b'Position')),
                ('audit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='audits.Audit')),
            ],
            options={
                'ordering': ['audit'],
                'verbose_name': 'Audit Group',
                'verbose_name_plural': 'Audit Groups',
            },
        ),
        migrations.CreateModel(
            name='AuditGroup2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True)),
                ('title', models.CharField(default=b'no group 2 title', max_length=512, verbose_name=b'Group 2 Title')),
                ('position', models.IntegerField(default=0, verbose_name=b'Position')),
                ('audit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group2s', to='audits.Audit')),
            ],
            options={
                'ordering': ['audit'],
                'verbose_name': 'Audit Group 2',
                'verbose_name_plural': 'Audit Group 2s',
            },
        ),
        migrations.CreateModel(
            name='AuditGroup2Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True)),
                ('title', models.CharField(default=b'no group group item title', max_length=512, verbose_name=b'Group2 Item Title')),
                ('group2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group2_items', to='audits.AuditGroup2')),
            ],
            options={
                'ordering': ['group2', 'group_item'],
                'verbose_name': 'Audit Group2 Item',
                'verbose_name_plural': 'Audit Groups2 Items',
            },
        ),
        migrations.CreateModel(
            name='AuditGroupItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True)),
                ('title', models.CharField(default=b'no group item title', max_length=512, verbose_name=b'Group Item Title')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_items', to='audits.AuditGroup')),
            ],
            options={
                'ordering': ['group'],
                'verbose_name': 'Audit Group Item',
                'verbose_name_plural': 'Audit Groups Items',
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=1024, verbose_name=b'Website URL')),
                ('title', models.CharField(default=b'no title', max_length=512, verbose_name=b'Website Title')),
                ('slug', models.SlugField(blank=True, max_length=128)),
                ('span_sub_domains', models.CharField(blank=True, default=b'', max_length=1024, verbose_name=b'Span Domains (space separated)')),
                ('exclude_sub_domains', models.CharField(blank=True, default=b'', max_length=1024, verbose_name=b'Exclude Domains (space separated)')),
                ('include_domains', models.CharField(blank=True, default=b'', max_length=1024, verbose_name=b'Include Domains (space separated)')),
                ('audit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='websites', to='audits.Audit')),
                ('group2_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='websites', to='audits.AuditGroup2Item')),
                ('group_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='websites', to='audits.AuditGroupItem')),
            ],
            options={
                'ordering': ['url'],
                'verbose_name': 'Website',
                'verbose_name_plural': 'Websites',
            },
        ),
        migrations.AddField(
            model_name='auditgroup2item',
            name='group_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group2_items', to='audits.AuditGroupItem'),
        ),
    ]
