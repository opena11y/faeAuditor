# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('markup', '0001_initial'),
        ('rulesets', '__first__'),
        ('wcag20', '__first__'),
        ('ruleCategories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuidelineRuleMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('guideline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcag20.Guideline')),
            ],
            options={
                'ordering': ['guideline'],
            },
        ),
        migrations.CreateModel(
            name='NodeResultMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('updated_date', models.DateTimeField(editable=False)),
                ('label', models.CharField(choices=[('ELEMENT_PASS_1', 'ELEMENT_PASS_1'), ('ELEMENT_PASS_2', 'ELEMENT_PASS_2'), ('ELEMENT_PASS_3', 'ELEMENT_PASS_3'), ('ELEMENT_PASS_4', 'ELEMENT_PASS_4'), ('ELEMENT_PASS_5', 'ELEMENT_PASS_5'), ('ELEMENT_FAIL_1', 'ELEMENT_FAIL_1'), ('ELEMENT_FAIL_2', 'ELEMENT_FAIL_2'), ('ELEMENT_FAIL_3', 'ELEMENT_FAIL_3'), ('ELEMENT_FAIL_4', 'ELEMENT_FAIL_4'), ('ELEMENT_FAIL_5', 'ELEMENT_FAIL_5'), ('ELEMENT_MC_1', 'ELEMENT_MC_1'), ('ELEMENT_MC_2', 'ELEMENT_MC_2'), ('ELEMENT_MC_3', 'ELEMENT_MC_3'), ('ELEMENT_MC_4', 'ELEMENT_MC_4'), ('ELEMENT_MC_5', 'ELEMENT_MC_5'), ('ELEMENT_HIDDEN_1', 'ELEMENT_HIDDEN_1'), ('ELEMENT_HIDDEN_2', 'ELEMENT_HIDDEN_2'), ('PAGE_PASS_1', 'PAGE_PASS_1'), ('PAGE_PASS_2', 'PAGE_PASS_2'), ('PAGE_PASS_3', 'PAGE_PASS_3'), ('PAGE_PASS_4', 'PAGE_PASS_4'), ('PAGE_PASS_5', 'PAGE_PASS_5'), ('PAGE_FAIL_1', 'PAGE_FAIL_1'), ('PAGE_FAIL_2', 'PAGE_FAIL_2'), ('PAGE_FAIL_3', 'PAGE_FAIL_3'), ('PAGE_FAIL_4', 'PAGE_FAIL_4'), ('PAGE_FAIL_5', 'PAGE_FAIL_5'), ('PAGE_MC_1', 'PAGE_MC_1'), ('PAGE_MC_2', 'PAGE_MC_2'), ('PAGE_MC_3', 'PAGE_MC_3'), ('PAGE_MC_4', 'PAGE_MC_4'), ('PAGE_MC_5', 'PAGE_MC_5'), ('WEBSITE_PASS_1', 'WEBSITE_PASS_1'), ('WEBSITE_PASS_2', 'WEBSITE_PASS_2'), ('WEBSITE_PASS_3', 'WEBSITE_PASS_3'), ('WEBSITE_PASS_4', 'WEBSITE_PASS_4'), ('WEBSITE_PASS_5', 'WEBSITE_PASS_5'), ('WEBSITE_FAIL_1', 'WEBSITE_FAIL_1'), ('WEBSITE_FAIL_2', 'WEBSITE_FAIL_2'), ('WEBSITE_FAIL_3', 'WEBSITE_FAIL_3'), ('WEBSITE_FAIL_4', 'WEBSITE_FAIL_4'), ('WEBSITE_FAIL_5', 'WEBSITE_FAIL_5'), ('WEBSITE_MC_1', 'WEBSITE_MC_1'), ('WEBSITE_MC_2', 'WEBSITE_MC_2'), ('WEBSITE_MC_3', 'WEBSITE_MC_3'), ('WEBSITE_MC_4', 'WEBSITE_MC_4'), ('WEBSITE_MC_5', 'WEBSITE_MC_5')], max_length=32, verbose_name='Label')),
                ('message', models.CharField(max_length=512, verbose_name='Message')),
            ],
            options={
                'ordering': ['label'],
                'verbose_name': 'Node Result Message',
                'verbose_name_plural': 'Node Result Message',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('updated_date', models.DateTimeField(editable=False)),
                ('rule_id', models.CharField(max_length=32, unique=True, verbose_name='Rule ID')),
                ('slug', models.SlugField(blank=True, default='none', max_length=32)),
                ('primary_property', models.CharField(default='', max_length=64, verbose_name='primary attribute or property used by the rule')),
                ('resource_properties', models.CharField(max_length=250, verbose_name='Comma separated list of cache properties and attributes used by the rule')),
                ('language_dependancy', models.CharField(default='', max_length=100, verbose_name='Language codes separated by commas')),
                ('validation', models.TextField(blank=True, null=True, verbose_name='Javascript code for validation function')),
                ('nls_rule_id', models.CharField(max_length=64, verbose_name='Translated Rule ID')),
                ('definition', models.CharField(max_length=512, verbose_name='Rule Definition')),
                ('definition_html', models.CharField(default='', max_length=512)),
                ('summary', models.CharField(max_length=128, verbose_name='Rule Summary (shorter version of definition)')),
                ('summary_html', models.CharField(default='', max_length=256)),
                ('summary_text', models.CharField(default='', max_length=128)),
                ('target_resource_desc', models.CharField(max_length=512, verbose_name='Summary of the types of element definitions this rule tests')),
                ('target_resource_desc_html', models.CharField(max_length=512)),
                ('purpose', models.TextField(default='', verbose_name='Purpose (i.e how does the rule help people with disabilites)')),
                ('purpose_html', models.TextField(default='')),
                ('techniques', models.TextField(default='', verbose_name='Techniques')),
                ('techniques_html', models.TextField(default='')),
                ('manual_checks', models.TextField(default='', verbose_name='Manual Checks')),
                ('manual_checks_html', models.TextField(default='')),
                ('informational_links', models.TextField(default='', verbose_name='Informational Links')),
                ('informational_links_html', models.TextField(default='')),
                ('rule_result_mc_s', models.CharField(blank=True, max_length=512, null=True, verbose_name='Rule Result Message: One manual check')),
                ('rule_result_mc_p', models.CharField(blank=True, max_length=512, null=True, verbose_name='Rule Result Message: More than one manual check')),
                ('rule_result_fail_s', models.CharField(blank=True, max_length=512, null=True, verbose_name='Rule Result Message: One failed element')),
                ('rule_result_fail_p', models.CharField(blank=True, max_length=512, null=True, verbose_name='Rule Result Message: More than one failed element')),
                ('rule_result_hidden_s', models.CharField(blank=True, max_length=512, null=True, verbose_name='Rule Result Message: One hidden element')),
                ('rule_result_hidden_p', models.CharField(blank=True, max_length=512, null=True, verbose_name='Rule Result Message: More than one hidden element')),
                ('rule_result_na', models.CharField(blank=True, max_length=512, null=True, verbose_name='Rule Result Message: Not Applicable Message')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rules', to='ruleCategories.RuleCategory')),
            ],
            options={
                'ordering': ['nls_rule_id'],
                'verbose_name': 'Rule',
                'verbose_name_plural': 'Rules',
            },
        ),
        migrations.CreateModel(
            name='RuleCategoryRuleMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rule_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruleCategories.RuleCategory')),
            ],
            options={
                'ordering': ['rule_category'],
            },
        ),
        migrations.CreateModel(
            name='RuleGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rule_group_code', models.IntegerField(default=0, verbose_name='Group Code')),
                ('title', models.CharField(default='none', max_length=32, verbose_name='Group Title')),
                ('description', models.CharField(default='', max_length=2048, verbose_name='Group Description')),
            ],
            options={
                'ordering': ['rule_group_code'],
                'verbose_name': 'Rule Group',
                'verbose_name_plural': 'Rule Groups',
            },
        ),
        migrations.CreateModel(
            name='RuleMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('required', models.BooleanField(default=True)),
                ('enabled', models.BooleanField(default=True)),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rule_mappings', to='rules.Rule')),
                ('ruleset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rule_mappings', to='rulesets.Ruleset')),
            ],
            options={
                'ordering': ['rule__nls_rule_id'],
            },
        ),
        migrations.CreateModel(
            name='RuleScope',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rule_scope_code', models.IntegerField(default=0, verbose_name='Scope Code')),
                ('slug', models.SlugField(blank=True, default='none', max_length=32)),
                ('title', models.CharField(default='none', max_length=128, verbose_name='Scope Title')),
                ('abbrev', models.CharField(default='none', max_length=32, verbose_name='Scope Abbreviation')),
                ('description', models.CharField(default='', max_length=2048, verbose_name='Scope Description')),
            ],
            options={
                'ordering': ['rule_scope_code'],
                'verbose_name': 'Rule Scope',
                'verbose_name_plural': 'Rule Scopes',
            },
        ),
        migrations.CreateModel(
            name='SuccessCriterionRuleMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('guideline_rule_mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sc_mappings', to='rules.GuidelineRuleMapping')),
                ('primary_mappings', models.ManyToManyField(related_name='primary_mappings', to='rules.RuleMapping')),
                ('related_mappings', models.ManyToManyField(related_name='related_mappings', to='rules.RuleMapping')),
                ('success_criterion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wcag20.SuccessCriterion')),
            ],
            options={
                'ordering': ['success_criterion'],
            },
        ),
        migrations.AddField(
            model_name='rulecategoryrulemapping',
            name='rule_mappings',
            field=models.ManyToManyField(to='rules.RuleMapping'),
        ),
        migrations.AddField(
            model_name='rulecategoryrulemapping',
            name='ruleset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rc_mappings', to='rulesets.Ruleset'),
        ),
        migrations.AddField(
            model_name='rule',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rules', to='rules.RuleGroup'),
        ),
        migrations.AddField(
            model_name='rule',
            name='scope',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rules', to='rules.RuleScope'),
        ),
        migrations.AddField(
            model_name='rule',
            name='target_resources',
            field=models.ManyToManyField(related_name='rules', to='markup.ElementDefinition'),
        ),
        migrations.AddField(
            model_name='rule',
            name='wcag_primary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rules', to='wcag20.SuccessCriterion'),
        ),
        migrations.AddField(
            model_name='rule',
            name='wcag_related',
            field=models.ManyToManyField(related_name='related_rules', to='wcag20.SuccessCriterion'),
        ),
        migrations.AddField(
            model_name='noderesultmessage',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node_result_messages', to='rules.Rule'),
        ),
        migrations.AddField(
            model_name='guidelinerulemapping',
            name='rule_mappings',
            field=models.ManyToManyField(to='rules.RuleMapping'),
        ),
        migrations.AddField(
            model_name='guidelinerulemapping',
            name='ruleset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gl_mappings', to='rulesets.Ruleset'),
        ),
        migrations.AlterUniqueTogether(
            name='rule',
            unique_together=set([('rule_id', 'definition')]),
        ),
    ]
