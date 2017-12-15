# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-02 20:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ruleCategories', '0001_initial'),
        ('wcag20', '0001_initial'),
        ('audits', '__first__'),
        ('rulesets', '0001_initial'),
        ('rules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditGuidelineResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=16)),
            ],
            options={
                'ordering': ['guideline'],
                'verbose_name': 'Audit Guideline Result',
                'verbose_name_plural': 'Audit Guideline Result',
            },
        ),
        migrations.CreateModel(
            name='AuditResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=512, verbose_name='Audit Result Title')),
                ('slug', models.SlugField(blank=True, default='none', editable=False, max_length=16)),
                ('depth', models.IntegerField(choices=[(1, 'Start URL only'), (2, 'First level links'), (3, 'Second level links')], default=2)),
                ('max_pages', models.IntegerField(choices=[(5, '   5 pages'), (10, '  10 pages'), (25, '  25 pages'), (50, '  50 pages'), (100, ' 100 pages'), (200, ' 200 pages'), (400, ' 400 pages'), (800, ' 800 pages')], default=200, verbose_name='Maximum Pages')),
                ('wait_time', models.IntegerField(choices=[(30000, ' 30 seconds'), (45000, ' 45 seconds'), (60000, ' 60 seconds'), (90000, ' 90 seconds'), (120000, '120 seconds')], default=30000)),
                ('browser_emulation', models.CharField(choices=[('Firefox', 'Mozilla Firefox'), ('IE', 'Microsoft Internet Explorer'), ('Chrome', 'Google Chrome')], default='Chrome', max_length=32, verbose_name='Browser Emulation')),
                ('follow', models.IntegerField(choices=[(1, 'Specified domain only'), (2, 'Next-level subdomains')], default=1, verbose_name='Follow Links in')),
                ('total_pages', models.IntegerField(default=0)),
                ('total_websites', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('-', 'Created'), ('I', 'Initalized'), ('A', 'Analyzing'), ('C', 'Complete'), ('E', 'Error'), ('D', 'Marked for deletion')], default='-', max_length=10, verbose_name='Status')),
                ('audit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audit_results', to='audits.Audit')),
                ('ruleset', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rulesets.Ruleset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Audit Result',
                'verbose_name_plural': 'Audit Results',
            },
        ),
        migrations.CreateModel(
            name='AuditRuleCategoryResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=16)),
                ('audit_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_rc_results', to='auditResults.AuditResult')),
                ('rule_category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ruleCategories.RuleCategory')),
            ],
            options={
                'ordering': ['rule_category'],
                'verbose_name': 'Audit Rule Category Result',
                'verbose_name_plural': 'Audit Rule Category Results',
            },
        ),
        migrations.CreateModel(
            name='AuditRuleResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=16)),
                ('pages_violation', models.IntegerField(default=0)),
                ('pages_warning', models.IntegerField(default=0)),
                ('pages_manual_check', models.IntegerField(default=0)),
                ('pages_passed', models.IntegerField(default=0)),
                ('pages_na', models.IntegerField(default=0)),
                ('pages_with_hidden_content', models.IntegerField(default=0)),
                ('audit_gl_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_rule_results', to='auditResults.AuditGuidelineResult')),
                ('audit_rc_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_rule_results', to='auditResults.AuditRuleCategoryResult')),
                ('audit_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_rule_results', to='auditResults.AuditResult')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditRuleScopeResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[('U', 'Undefined'), ('NA', 'Not applicable'), ('NI', 'Not Implemented'), ('PI', 'Partial Implementation'), ('AC', 'Almost Complete'), ('NI-MC', 'Not Implemented with manual checks required'), ('PI-MC', 'Partial Implementation with manual checks required'), ('AC-MC', 'Almost Complete with manual checks required'), ('C', 'Complete')], default='U', max_length=8, verbose_name='Implementation Status')),
                ('manual_check_status', models.CharField(choices=[('NC', 'Not Checked'), ('NA', 'Not Applicable'), ('P', 'Passed'), ('F', 'Fail')], default='NC', max_length=2, verbose_name='Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=16)),
                ('audit_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_rs_results', to='auditResults.AuditResult')),
                ('rule_scope', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rules.RuleScope')),
            ],
            options={
                'ordering': ['-rule_scope'],
                'verbose_name': 'Website Rule Scope Result',
                'verbose_name_plural': 'Website Rule Scope Results',
            },
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='audit_rs_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_rule_results', to='auditResults.AuditRuleScopeResult'),
        ),
        migrations.AddField(
            model_name='auditruleresult',
            name='rule',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rules.Rule'),
        ),
        migrations.AddField(
            model_name='auditguidelineresult',
            name='audit_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audit_gl_results', to='auditResults.AuditResult'),
        ),
        migrations.AddField(
            model_name='auditguidelineresult',
            name='guideline',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wcag20.Guideline'),
        ),
    ]
