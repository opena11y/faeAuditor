# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-08 20:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_start', models.DateField(blank=True, null=True)),
                ('subscription_end', models.DateField(blank=True, null=True)),
                ('subscription_payments', models.IntegerField(default=0)),
                ('subscription_daily_rate', models.IntegerField(default=0)),
                ('subscription_status', models.CharField(choices=[('FREE', 'Free'), ('CURRENT', 'Current'), ('EXPIRED', 'Expired')], default='CURRENT', max_length=8)),
                ('subscription_days', models.IntegerField(default=0)),
                ('org', models.CharField(blank=True, max_length=128)),
                ('dept', models.CharField(blank=True, max_length=128)),
                ('email_announcements', models.BooleanField(default=True)),
                ('timezone', timezone_field.fields.TimeZoneField(default='America/Chicago')),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profiles', to='accounts.AccountType')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
