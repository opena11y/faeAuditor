"""
Copyright 2014-2016 University of Illinois

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

file: websiteResults/admin.py

Author: Jon Gunderson

"""

from __future__ import absolute_import
from django.contrib import admin


from .models import AuditResult
from .models import AuditRuleCategoryResult
from .models import AuditGuidelineResult
from .models import AuditRuleScopeResult
from .models import AuditRuleResult


class AuditResultAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'depth', 'created', 'website_count', 'page_count', 'rules_violation', 'rules_warning', 'rules_manual_check', 'rules_passed', 'implementation_pass_fail_score', 'implementation_pass_fail_status', 'implementation_score', 'implementation_score_fail', 'implementation_score_mc', 'implementation_status', 'has_manual_checks', 'implementation_pass_fail_summ', 'implementation_summ', 'total_pages', 'ruleset')
    list_filter  = ('audit', )

admin.site.register(AuditResult, AuditResultAdmin)

class AuditRuleCategoryResultAdmin(admin.ModelAdmin):
    list_display = ('rule_category', 'slug', 'audit_result', 'rules_violation', 'rules_warning', 'rules_manual_check', 'rules_passed', 'implementation_pass_fail_score', 'implementation_score', 'implementation_score_fail', 'implementation_score_mc', 'implementation_status', 'has_manual_checks', 'implementation_pass_fail_summ', 'implementation_summ', 'total_pages')
    list_filter  = ('audit_result', 'rule_category')

admin.site.register(AuditRuleCategoryResult, AuditRuleCategoryResultAdmin)

class AuditGuidelineResultAdmin(admin.ModelAdmin):
    list_display = ('guideline', 'slug', 'audit_result', 'rules_violation', 'rules_warning', 'rules_manual_check', 'rules_passed', 'implementation_pass_fail_score', 'implementation_score', 'implementation_score_fail', 'implementation_score_mc', 'implementation_status', 'has_manual_checks', 'implementation_pass_fail_summ', 'implementation_summ', 'total_pages')
    list_filter  = ('audit_result', 'guideline')

admin.site.register(AuditGuidelineResult, AuditGuidelineResultAdmin)

class AuditRuleScopeResultAdmin(admin.ModelAdmin):
    list_display = ('rule_scope', 'slug', 'audit_result', 'rules_violation', 'rules_warning', 'rules_manual_check', 'rules_passed', 'implementation_pass_fail_score', 'implementation_score', 'implementation_score_fail', 'implementation_score_mc', 'implementation_status', 'has_manual_checks', 'implementation_pass_fail_summ', 'implementation_summ', 'total_pages')
    list_filter  = ('audit_result', 'rule_scope')

admin.site.register(AuditRuleScopeResult, AuditRuleScopeResultAdmin)

class AuditRuleResultAdmin(admin.ModelAdmin):
    list_display = ('rule', 'audit_result', 'result_value', 'websites_violation', 'websites_warning', 'websites_manual_check', 'websites_passed', 'websites_na', 'pages_violation', 'pages_warning', 'pages_manual_check', 'pages_passed', 'pages_na', 'elements_violation', 'elements_warning', 'elements_mc_identified', 'elements_passed', 'elements_hidden', 'implementation_pass_fail_score', 'implementation_score', 'implementation_score_fail', 'implementation_score_mc', 'implementation_status')
    list_filter  = ('audit_result', 'rule')

admin.site.register(AuditRuleResult, AuditRuleResultAdmin)


