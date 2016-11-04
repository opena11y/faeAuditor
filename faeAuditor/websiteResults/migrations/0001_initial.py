# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 18:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ruleCategories', '0001_initial'),
        ('rules', '0001_initial'),
        ('wcag20', '0001_initial'),
        ('auditGroupResults', '0001_initial'),
        ('auditGroup2Results', '0001_initial'),
        ('rulesets', '0001_initial'),
        ('auditResults', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilteredURL',
            fields=[
                ('filtered_url_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=4096, verbose_name=b'Other URL')),
                ('url_referenced', models.URLField(max_length=4096, verbose_name=b'Referenced URL')),
            ],
            options={
                'ordering': ['url_referenced', 'url'],
                'verbose_name': 'URL: Filtered',
                'verbose_name_plural': 'URL: Filtered',
            },
        ),
        migrations.CreateModel(
            name='ProcessedURL',
            fields=[
                ('processed_url_id', models.AutoField(primary_key=True, serialize=False)),
                ('page_seq_num', models.IntegerField(default=-1)),
                ('url_requested', models.URLField(max_length=4096, verbose_name=b'Processed URL')),
                ('url_returned', models.URLField(max_length=4096, verbose_name=b'Returned URL')),
                ('redirect', models.BooleanField(default=False, verbose_name=b'Server redirect')),
                ('http_status_code', models.IntegerField(verbose_name=b'http status code')),
                ('url_referenced', models.URLField(max_length=4096, verbose_name=b'Referenced URL')),
                ('dom_time', models.IntegerField(verbose_name=b'Loading DOM time')),
                ('link_time', models.IntegerField(verbose_name=b'Retreive links tIme')),
                ('event_time', models.IntegerField(verbose_name=b'Event time')),
                ('eval_time', models.IntegerField(verbose_name=b'Evaluation time')),
                ('save_time', models.IntegerField(verbose_name=b'Saving results time')),
                ('total_time', models.IntegerField(verbose_name=b'Total processing time')),
            ],
            options={
                'ordering': ['http_status_code', 'url_returned', 'total_time'],
                'verbose_name': 'URL: Processed',
                'verbose_name_plural': 'URL: Processed',
            },
        ),
        migrations.CreateModel(
            name='UnprocessedURL',
            fields=[
                ('unprocessed_url_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=4096, verbose_name=b'Unprocessed URL')),
                ('url_referenced', models.URLField(max_length=4096, verbose_name=b'Referenced URL')),
                ('dom_time', models.IntegerField(verbose_name=b'Loading DOM time')),
                ('link_time', models.IntegerField(verbose_name=b'Retreive links tIme')),
                ('event_time', models.IntegerField(verbose_name=b'Event time')),
                ('eval_time', models.IntegerField(verbose_name=b'Evaluation time')),
                ('save_time', models.IntegerField(verbose_name=b'Saving results time')),
                ('total_time', models.IntegerField(verbose_name=b'Total processing time')),
            ],
            options={
                'ordering': ['url', 'url_referenced'],
                'verbose_name': 'URL: Unprocessed',
                'verbose_name_plural': 'URL: Unprocessed',
            },
        ),
        migrations.CreateModel(
            name='WebsiteGuidelineResult',
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
                ('slug', models.SlugField(blank=True, default=b'none', editable=False, max_length=16)),
                ('guideline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wcag20.Guideline')),
            ],
            options={
                'ordering': ['guideline'],
                'verbose_name': 'Website Guideline Result',
                'verbose_name_plural': 'Website Guideline Results',
            },
        ),
        migrations.CreateModel(
            name='WebsiteResult',
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
                ('slug', models.SlugField(blank=True, default=b'', editable=False, max_length=256, unique=True)),
                ('title', models.CharField(default=b'', max_length=1024, verbose_name=b'Title')),
                ('url', models.URLField(default=b'', max_length=1024, verbose_name=b'URL')),
                ('follow', models.IntegerField(choices=[(1, b'Specified domain only'), (2, b'Next-level subdomains')], default=1, verbose_name=b'Follow Links in')),
                ('depth', models.IntegerField(choices=[(1, b'Start URL only'), (2, b'First level links'), (3, b'Second level links')], default=2, verbose_name=b'Depth of Evaluation')),
                ('max_pages', models.IntegerField(choices=[(5, b'   5 pages'), (10, b'  10 pages'), (25, b'  25 pages'), (50, b'  50 pages'), (100, b' 100 pages'), (200, b' 200 pages'), (400, b' 400 pages'), (800, b' 800 pages')], default=0, verbose_name=b'Maximum Pages')),
                ('browser_emulation', models.CharField(default=b'FIREFOX', max_length=32, verbose_name=b'Browser Emulation')),
                ('wait_time', models.IntegerField(choices=[(30000, b' 30 seconds'), (45000, b' 45 seconds'), (60000, b' 60 seconds'), (90000, b' 90 seconds'), (120000, b'120 seconds')], default=90000, verbose_name=b'How long to wait for website to load resources')),
                ('span_sub_domains', models.CharField(blank=True, default=b'', max_length=1024, verbose_name=b'Span Sub-Domains (space separated)')),
                ('exclude_sub_domains', models.CharField(blank=True, default=b'', max_length=1024, verbose_name=b'Exclude Sub-Domains (space separated)')),
                ('include_domains', models.CharField(blank=True, default=b'', max_length=1024, verbose_name=b'Include Domains (space separated)')),
                ('authorization', models.TextField(blank=True, default=b'', max_length=8192, verbose_name=b'Authentication Information')),
                ('page_count', models.IntegerField(default=0, verbose_name=b'Number of Pages')),
                ('archive', models.BooleanField(default=False)),
                ('delete_flag', models.BooleanField(default=False)),
                ('stats', models.BooleanField(default=False)),
                ('last_viewed', models.DateTimeField(auto_now=True)),
                ('last_report_type', models.CharField(choices=[(b'rules', b'Summary'), (b'pages', b'All Pages'), (b'page', b'Page')], default=b'rules', max_length=16, verbose_name=b'Last Report Type')),
                ('last_view', models.CharField(choices=[(b'rc', b'Rule Category'), (b'gl', b'WCAG Guideline'), (b'rs', b'Rule Scope')], default=b'rc', max_length=4, verbose_name=b'Last Viewed')),
                ('last_group', models.CharField(default=b'', max_length=32, verbose_name=b'Last Group')),
                ('last_page', models.IntegerField(default=1, verbose_name=b'Last Page Viewed')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[(b'-', b'Created'), (b'I', b'Initalized'), (b'A', b'Analyzing'), (b'S', b'Saving'), (b'C', b'Complete'), (b'E', b'Error'), (b'D', b'Marked for deletion'), (b'SUM', b'Archived for summary stats')], default=b'-', max_length=10, verbose_name=b'Status')),
                ('processing_time', models.IntegerField(default=-1)),
                ('processed_urls_count', models.IntegerField(default=-1)),
                ('unprocessed_urls_count', models.IntegerField(default=-1)),
                ('filtered_urls_count', models.IntegerField(default=-1)),
                ('data_dir_slug', models.SlugField(editable=False)),
                ('data_directory', models.CharField(default=b'', max_length=1024, verbose_name=b'Data Directory')),
                ('data_property_file', models.CharField(default=b'', max_length=1024, verbose_name=b'Property File Name')),
                ('data_authorization_file', models.CharField(blank=True, default=b'', max_length=1024, verbose_name=b'Authorization File Name')),
                ('data_multiple_urls_file', models.CharField(blank=True, default=b'', max_length=1024, verbose_name=b'Multiple URLs File Name')),
                ('log_file', models.CharField(default=b'', max_length=1024, verbose_name=b'Log file')),
                ('audit_group2_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_reports', to='auditGroup2Results.AuditGroup2Result')),
                ('audit_group_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_reports', to='auditGroupResults.AuditGroupResult')),
                ('audit_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_reports', to='auditResults.AuditResult')),
                ('ruleset', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rulesets.Ruleset')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ws_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-archive', '-created'],
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
        migrations.CreateModel(
            name='WebsiteRuleCategoryResult',
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
                ('slug', models.SlugField(blank=True, default=b'none', editable=False, max_length=16)),
                ('rule_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ruleCategories.RuleCategory')),
                ('ws_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_rc_results', to='websiteResults.WebsiteResult')),
            ],
            options={
                'ordering': ['rule_category'],
                'verbose_name': 'Website Rule Category Result',
                'verbose_name_plural': 'Website Rule Category Results',
            },
        ),
        migrations.CreateModel(
            name='WebsiteRuleResult',
            fields=[
                ('result_value', models.IntegerField(default=0)),
                ('implementation_pass_fail_score', models.IntegerField(default=-1)),
                ('implementation_score', models.IntegerField(default=-1)),
                ('implementation_pass_fail_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Pass/Fail Status')),
                ('implementation_status', models.CharField(choices=[(b'U', b'Undefined'), (b'NA', b'Not applicable'), (b'NI', b'Not Implemented'), (b'PI', b'Partial Implementation'), (b'AC', b'Almost Complete'), (b'NI-MC', b'Not Implemented with manual checks required'), (b'PI-MC', b'Partial Implementation with manual checks required'), (b'AC-MC', b'Almost Complete with manual checks required'), (b'C', b'Complete')], default=b'U', max_length=8, verbose_name=b'Implementation Status')),
                ('manual_check_status', models.CharField(choices=[(b'NC', b'Not Checked'), (b'NA', b'Not Applicable'), (b'P', b'Passed'), (b'F', b'Fail')], default=b'NC', max_length=2, verbose_name=b'Manual Check Status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, default=b'none', editable=False, max_length=16)),
                ('rule_required', models.BooleanField(default=False)),
                ('rule_number', models.IntegerField(default=-1)),
                ('pages_violation', models.IntegerField(default=0)),
                ('pages_warning', models.IntegerField(default=0)),
                ('pages_manual_check', models.IntegerField(default=0)),
                ('pages_passed', models.IntegerField(default=0)),
                ('pages_na', models.IntegerField(default=0)),
                ('elements_violation', models.IntegerField(default=0)),
                ('elements_warning', models.IntegerField(default=0)),
                ('elements_mc_identified', models.IntegerField(default=0)),
                ('elements_mc_passed', models.IntegerField(default=0)),
                ('elements_mc_failed', models.IntegerField(default=0)),
                ('elements_mc_na', models.IntegerField(default=0)),
                ('elements_passed', models.IntegerField(default=0)),
                ('elements_hidden', models.IntegerField(default=0)),
                ('pages_with_hidden_content', models.IntegerField(default=0)),
                ('rule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rules.Rule')),
                ('ws_gl_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ws_rule_results', to='websiteResults.WebsiteGuidelineResult')),
                ('ws_rc_result', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ws_rule_results', to='websiteResults.WebsiteRuleCategoryResult')),
                ('ws_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_rule_results', to='websiteResults.WebsiteResult')),
            ],
            options={
                'ordering': ['-pages_violation', '-pages_warning', '-pages_manual_check', '-pages_passed', '-pages_with_hidden_content', '-rule__scope'],
                'verbose_name': 'Website Rule Result',
                'verbose_name_plural': 'Website Rule Results',
            },
        ),
        migrations.CreateModel(
            name='WebsiteRuleScopeResult',
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
                ('slug', models.SlugField(blank=True, default=b'none', editable=False, max_length=16)),
                ('rule_scope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rules.RuleScope')),
                ('ws_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_rs_results', to='websiteResults.WebsiteResult')),
            ],
            options={
                'ordering': ['-rule_scope'],
                'verbose_name': 'Website Rule Scope Result',
                'verbose_name_plural': 'Website Rule Scope Results',
            },
        ),
        migrations.AddField(
            model_name='websiteruleresult',
            name='ws_rs_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ws_rule_results', to='websiteResults.WebsiteRuleScopeResult'),
        ),
        migrations.AddField(
            model_name='websiteguidelineresult',
            name='ws_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ws_gl_results', to='websiteResults.WebsiteResult'),
        ),
        migrations.AddField(
            model_name='unprocessedurl',
            name='ws_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unprocessed_urls', to='websiteResults.WebsiteResult'),
        ),
        migrations.AddField(
            model_name='processedurl',
            name='ws_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processed_urls', to='websiteResults.WebsiteResult'),
        ),
        migrations.AddField(
            model_name='filteredurl',
            name='ws_report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filtered_urls', to='websiteResults.WebsiteResult'),
        ),
    ]
