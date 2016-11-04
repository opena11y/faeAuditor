# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('audits', '__first__'),
        ('ruleCategories', '__first__'),
        ('auditGroupResults', '__first__'),
        ('wcag20', '__first__'),
        ('rules', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditGroup2GuidelineResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
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
                'verbose_name': 'Group2 Guideline Result',
                'verbose_name_plural': 'Group2 Guideline Result',
            },
        ),
        migrations.CreateModel(
            name='AuditGroup2Result',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='none', editable=False, max_length=16)),
                ('total_pages', models.IntegerField(default=0)),
                ('total_websites', models.IntegerField(default=0)),
                ('group2_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audits.AuditGroup2Item')),
                ('group_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group2_results', to='auditGroupResults.AuditGroupResult')),
            ],
            options={
                'verbose_name': 'Group2 Result',
                'verbose_name_plural': 'Group2 Results',
            },
        ),
        migrations.CreateModel(
            name='AuditGroup2RuleCategoryResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=16)),
                ('group2_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group2_rc_results', to='auditGroup2Results.AuditGroup2Result')),
                ('rule_category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ruleCategories.RuleCategory')),
            ],
            options={
                'ordering': ['rule_category'],
                'verbose_name': 'Group2 Rule Category Result',
                'verbose_name_plural': 'Group2 Rule Category Results',
            },
        ),
        migrations.CreateModel(
            name='AuditGroup2RuleResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=16)),
                ('pages_violation', models.IntegerField(default=0)),
                ('pages_warning', models.IntegerField(default=0)),
                ('pages_manual_check', models.IntegerField(default=0)),
                ('pages_passed', models.IntegerField(default=0)),
                ('pages_na', models.IntegerField(default=0)),
                ('pages_with_hidden_content', models.IntegerField(default=0)),
                ('group2_gl_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group2_rule_results', to='auditGroup2Results.AuditGroup2GuidelineResult')),
                ('group2_rc_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group2_rule_results', to='auditGroup2Results.AuditGroup2RuleCategoryResult')),
                ('group2_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group2_rule_results', to='auditGroupResults.AuditGroupResult')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditGroup2RuleScopeResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
                ('rules_violation', models.IntegerField(default=0)),
                ('rules_warning', models.IntegerField(default=0)),
                ('rules_manual_check', models.IntegerField(default=0)),
                ('rules_passed', models.IntegerField(default=0)),
                ('rules_na', models.IntegerField(default=0)),
                ('rules_with_hidden_content', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=16)),
                ('group2_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group2_rs_results', to='auditGroup2Results.AuditGroup2Result')),
                ('rule_scope', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rules.RuleScope')),
            ],
            options={
                'ordering': ['-rule_scope'],
                'verbose_name': 'Group2 Rule Scope Result',
                'verbose_name_plural': 'Group2 Rule Scope Results',
            },
        ),
        migrations.AddField(
            model_name='auditgroup2ruleresult',
            name='group2_rs_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group2_rule_results', to='auditGroup2Results.AuditGroup2RuleScopeResult'),
        ),
        migrations.AddField(
            model_name='auditgroup2ruleresult',
            name='rule',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rules.Rule'),
        ),
        migrations.AddField(
            model_name='auditgroup2guidelineresult',
            name='group2_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group2_gl_results', to='auditGroup2Results.AuditGroup2Result'),
        ),
        migrations.AddField(
            model_name='auditgroup2guidelineresult',
            name='guideline',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wcag20.Guideline'),
        ),
    ]
