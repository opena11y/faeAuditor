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

file: auditResults/views.py

Author: Jon Gunderson

"""

from __future__ import absolute_import

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import redirect

from django.contrib import messages

from itertools import chain

from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import RedirectView

from audits.resultNavigationMixin import ResultNavigationMixin

from django.contrib.auth.models import User

from rules.models  import Rule
from audits.models import Audit

from .models       import AuditResult
from .models       import AuditGuidelineResult
from .models       import AuditRuleCategoryResult
from .models       import AuditRuleScopeResult
from .models       import AuditRuleResult

from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

from auditGroupResults.models  import AuditGroupResult
from auditGroupResults.models  import AuditGroupRuleResult

from auditGroup2Results.models import AuditGroup2Result
from auditGroup2Results.models import AuditGroup2RuleResult

from websiteResults.models     import WebsiteResult
from websiteResults.models     import WebsiteRuleResult

from pageResults.models     import PageResult
from pageResults.models     import PageRuleResult

from ruleCategories.models import RuleCategory
from wcag20.models         import Guideline
from rules.models          import RuleScope
from contacts.models       import Announcement

class AllRulesResultView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/all_rules_result.html'

    def get_context_data(self, **kwargs):
        context = super(AllRulesResultView, self).get_context_data(**kwargs)

        result_slug    = kwargs['result_slug']
        rule_grouping  = kwargs['rule_grouping']

        ar = AuditResult.objects.get(slug=result_slug)

        if rule_grouping == 'gl':
            rule_grouping_label = "Guideline"
            rule_group_results = ar.audit_gl_results.all()
        else:
            if rule_grouping == 'rs':
                rule_grouping_label = "Rule Scope"
                rule_group_results = ar.audit_rs_results.all()
            else:
                rule_grouping_label = "Rule Category"
                rule_group_results = ar.audit_rc_results.all()

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, None)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']     = ar.audit.slug
        context['result_slug']    = result_slug
        context['rule_grouping']  = rule_grouping

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_grouping_label'] = rule_grouping_label
        context['rule_group_results'] = rule_group_results

        return context

class RuleGroupResultView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultView, self).get_context_data(**kwargs)

        result_slug    = kwargs['result_slug']
        rule_grouping  = kwargs['rule_grouping']
        rule_group_slug    = kwargs['rule_group_slug']

        ar = AuditResult.objects.get(slug=result_slug)

        if rule_grouping == 'gl':
            rule_group_label  = Guideline.objects.get(slug=rule_group_slug).title
            rule_group_result = ar.audit_gl_results.get(slug=rule_group_slug)
        else:
            if rule_grouping == 'rs':
                rule_group_label  = RuleScope.objects.get(slug=rule_group_slug).title
                rule_group_result = ar.audit_rs_results.get(slug=rule_group_slug)
            else:
                rule_group_label  = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_group_result = ar.audit_rc_results.get(slug=rule_group_slug)

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']      = ar.audit.slug
        context['result_slug']     = result_slug
        context['rule_grouping']   = rule_grouping
        context['rule_group_slug'] = rule_group_slug

        # objects for rendering content
        context['audit_result']       = ar

        context['rule_group_label']    = rule_group_label
        context['rule_group_result']   = rule_group_result

        return context

class RuleGroupResultRuleView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleView, self).get_context_data(**kwargs)

        result_slug     = kwargs['result_slug']
        rule_grouping   = kwargs['rule_grouping']
        rule_group_slug = kwargs['rule_group_slug']
        rule_slug       = kwargs['rule_slug']

        ar  = AuditResult.objects.get(slug=result_slug)
        arr = AuditRuleResult.objects.get(audit_result=ar, slug=rule_slug)

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping       = 'rc'

        wsrrs  = WebsiteRuleResult.objects.filter(ws_report__audit_result=ar, slug=rule_slug)

        for wsrr in wsrrs:
            wsrr.href = reverse('rule_group_result_rule_website', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, wsrr.ws_report.slug])

        # Check if audit has audit grouping
        if ar.audit.groups.count():
            agrrs  = AuditGroupRuleResult.objects.filter(group_result__audit_result=ar, slug=rule_slug)
            for agrr in agrrs:
                agrr.href = reverse('rule_group_result_rule_audit_group', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, agrr.group_result.slug])
        else:
            agrrs = []

        # Check if audit has audit sub grouping
        if ar.audit.group2s.count():
            ag2rrs = AuditGroup2RuleResult.objects.filter(group2_result__group_result__audit_result=ar, slug=rule_slug)
            for ag2rr in ag2rrs:
                ag2rr.href = reverse('rule_group_result_rule_audit_group2', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, ag2rr.group2_result.slug])
        else:
            ag2rrs = []

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']      = ar.audit.slug
        context['result_slug']     = result_slug
        context['rule_grouping']   = rule_grouping
        context['rule_group_slug'] = rule_group_slug
        context['rule_slug']       = rule_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule']                      = Rule.objects.get(slug=rule_slug)
        context['rule_group_label']          = rule_group_label
        context['audit_result']              = ar
        context['audit_rule_result']         = arr
        context['audit_group_rule_results']  = agrrs
        context['audit_group2_rule_results'] = ag2rrs
        context['website_rule_results']      = wsrrs

        return context


class RuleGroupResultRuleWebsiteView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_website.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleWebsiteView, self).get_context_data(**kwargs)

        result_slug     = kwargs['result_slug']
        rule_grouping   = kwargs['rule_grouping']
        rule_group_slug = kwargs['rule_group_slug']
        rule_slug       = kwargs['rule_slug']
        website_slug    = kwargs['website_slug']

        ar   = AuditResult.objects.get(slug=result_slug)
        wsr  = ar.ws_results.get(slug=website_slug)
        wsrr = wsr.ws_rule_results.get(slug=rule_slug)
        prrs = wsrr.page_rule_results.all()

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'


        for prr in prrs:
            prr.href  = reverse('rule_group_result_rule_website_page', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, website_slug, prr.page_result.page_number])

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_website_page(website_slug)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']      = ar.audit.slug
        context['result_slug']     = result_slug
        context['rule_grouping']   = rule_grouping
        context['rule_group_slug'] = rule_group_slug
        context['rule_slug']       = rule_slug
        context['website_slug']    = website_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                 = Rule.objects.get(slug=rule_slug)
        context['website_result']       = wsr
        context['website_rule_result']  = wsrr
        context['page_rule_results']    = prrs

        return context

class RuleGroupResultRuleWebsitePageView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_website_page.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleWebsitePageView, self).get_context_data(**kwargs)

        result_slug     = kwargs['result_slug']
        rule_grouping   = kwargs['rule_grouping']
        rule_group_slug = kwargs['rule_group_slug']
        rule_slug       = kwargs['rule_slug']
        website_slug    = kwargs['website_slug']
        page_num        = kwargs['page_num']

        ar   = AuditResult.objects.get(slug=result_slug)
        wsr  = ar.ws_results.get(slug=website_slug)
        wsrr = wsr.ws_rule_results.get(slug=rule_slug)
        pr   = wsr.page_all_results.get(page_number=page_num)
        prr  = pr.page_rule_results.get(slug=rule_slug)

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_website_page(website_slug, page_num, wsr.page_count)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']      = ar.audit.slug
        context['result_slug']     = result_slug
        context['rule_grouping']   = rule_grouping
        context['rule_group_slug'] = rule_group_slug
        context['rule_slug']       = rule_slug
        context['website_slug']    = website_slug
        context['page_num']        = page_num

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                = Rule.objects.get(slug=rule_slug)
        context['website_result']          = wsr
        context['website_rule_result']     = wsrr
        context['page_result']             = pr
        context['page_rule_result']        = prr

        return context

class RuleGroupResultRuleAuditGroupView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_audit_group.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleAuditGroupView, self).get_context_data(**kwargs)

        result_slug       = kwargs['result_slug']
        rule_grouping     = kwargs['rule_grouping']
        rule_group_slug   = kwargs['rule_group_slug']
        rule_slug         = kwargs['rule_slug']
        audit_group_slug  = kwargs['audit_group_slug']

        ar   = AuditResult.objects.get(slug=result_slug)
        agr  = AuditGroupResult.objects.get(audit_result=ar, slug=audit_group_slug)
        agrr = agr.group_rule_results.get(slug=rule_slug)

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'


        ag2rrs = AuditGroup2RuleResult.objects.filter(group2_result__group_result__audit_result=ar, group2_result__group_result__slug=audit_group_slug, slug=rule_slug)

        for ag2rr in ag2rrs:
            ag2rr.href = reverse('rule_group_result_rule_audit_group_audit_group2', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, audit_group_slug, ag2rr.group2_result.slug])

        wsrrs = WebsiteRuleResult.objects.filter(ws_report__audit_result=ar, ws_report__group_result=agr, slug=rule_slug)

        for wsrr in wsrrs:
            wsrr.href = reverse('rule_group_result_rule_audit_group_website', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, audit_group_slug, wsrr.ws_report.slug])

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_audit_groups(audit_group_slug, None)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()


        # slugs used for urls
        context['audit_slug']        = ar.audit.slug
        context['result_slug']       = result_slug
        context['rule_grouping']     = rule_grouping
        context['rule_group_slug']   = rule_group_slug
        context['rule_slug']         = rule_slug
        context['audit_group_slug']  = audit_group_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                       = Rule.objects.get(slug=rule_slug)
        context['audit_group_result']         = agr
        context['audit_group_rule_result']    = agrr
        context['audit_group2_rule_results']  = ag2rrs
        context['website_rule_results']       = wsrrs

        return context

class RuleGroupResultRuleAuditGroupWebsiteView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_audit_group_website.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleAuditGroupWebsiteView, self).get_context_data(**kwargs)

        result_slug       = kwargs['result_slug']
        rule_grouping     = kwargs['rule_grouping']
        rule_group_slug   = kwargs['rule_group_slug']
        rule_slug         = kwargs['rule_slug']
        audit_group_slug  = kwargs['audit_group_slug']
        website_slug      = kwargs['website_slug']

        ar    = AuditResult.objects.get(slug=result_slug)
        agr = AuditGroupResult.objects.get(audit_result=ar, slug=audit_group_slug)
        wsrr  = WebsiteRuleResult.objects.get(ws_report__audit_result=ar, ws_report__slug=website_slug, slug=rule_slug)
        prrs  = wsrr.page_rule_results.all()

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'

        for prr in prrs:
            prr.href = reverse('rule_group_result_rule_audit_group_website_page', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, audit_group_slug, website_slug, prr.page_result.page_number])

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_audit_groups(audit_group_slug, None)
        self.result_nav.set_website_page(website_slug)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()


        # slugs used for urls
        context['audit_slug']        = ar.audit.slug
        context['result_slug']       = result_slug
        context['rule_grouping']     = rule_grouping
        context['rule_group_slug']   = rule_group_slug
        context['rule_slug']         = rule_slug
        context['audit_group_slug']  = audit_group_slug
        context['website_slug']      = website_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                = Rule.objects.get(slug=rule_slug)
        context['audit_group_result']  = agr
        context['website_rule_result'] = wsrr
        context['page_rule_results']   = prrs

        return context

class RuleGroupResultRuleAuditGroupWebsitePageView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_audit_group_website_page.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleAuditGroupWebsitePageView, self).get_context_data(**kwargs)


        result_slug       = kwargs['result_slug']
        rule_grouping     = kwargs['rule_grouping']
        rule_group_slug   = kwargs['rule_group_slug']
        rule_slug         = kwargs['rule_slug']
        audit_group_slug  = kwargs['audit_group_slug']
        website_slug      = kwargs['website_slug']
        page_num          = kwargs['page_num']

        ar   = AuditResult.objects.get(slug=result_slug)
        agr  = AuditGroupResult.objects.get(audit_result=ar, slug=audit_group_slug)
        wsrr = WebsiteRuleResult.objects.get(ws_report__audit_result=ar, ws_report__slug=website_slug, slug=rule_slug)

        pr   = PageResult.objects.get(ws_report__audit_result=ar, ws_report__slug=website_slug, page_number=page_num)
        prr  = pr.page_rule_results.get(slug=rule_slug)

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_audit_groups(audit_group_slug, None)
        self.result_nav.set_website_page(website_slug, page_num, wsrr.ws_report.page_count)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']      = ar.audit.slug
        context['result_slug']     = result_slug
        context['rule_grouping']   = rule_grouping
        context['rule_group_slug'] = rule_group_slug
        context['rule_slug']       = rule_slug
        context['website_slug']    = website_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                 = Rule.objects.get(slug=rule_slug)

        context['audit_group_result']   = agr
        context['website_rule_result']  = wsrr
        context['page_result']          = pr
        context['page_rule_result']     = prr

        return context

class RuleGroupResultRuleAuditGroupAuditGroup2View(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_audit_group_audit_group2.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleAuditGroupAuditGroup2View, self).get_context_data(**kwargs)


        result_slug       = kwargs['result_slug']
        rule_grouping     = kwargs['rule_grouping']
        rule_group_slug   = kwargs['rule_group_slug']
        rule_slug         = kwargs['rule_slug']
        audit_group_slug  = kwargs['audit_group_slug']
        audit_group2_slug = kwargs['audit_group2_slug']

        ar    = AuditResult.objects.get(slug=result_slug)
        ag2r  = AuditGroup2Result.objects.get(group_result__audit_result=ar, slug=audit_group2_slug)
        ag2rr = ag2r.group2_rule_results.get(slug=rule_slug)

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'


        wsrrs = WebsiteRuleResult.objects.filter(ws_report__audit_result=ar, ws_report__group2_result__slug=audit_group2_slug, slug=rule_slug)
        for wsrr in wsrrs:
            wsrr.href = reverse('rule_group_result_rule_audit_group_audit_group2_website', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, audit_group_slug, audit_group2_slug, wsrr.ws_report.slug])

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_audit_groups(audit_group_slug, audit_group2_slug)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']        = ar.audit.slug
        context['result_slug']       = result_slug
        context['rule_grouping']     = rule_grouping
        context['rule_group_slug']   = rule_group_slug
        context['rule_slug']         = rule_slug
        context['audit_group_slug']  = audit_group_slug
        context['audit_group2_slug'] = audit_group2_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                  = Rule.objects.get(slug=rule_slug)

        context['audit_group2_result']      = ag2r
        context['audit_group2_rule_result'] = ag2rr
        context['website_rule_results']     = wsrrs

        return context

class RuleGroupResultRuleAuditGroupAuditGroup2WebsiteView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_audit_group_audit_group2_website.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleAuditGroupAuditGroup2WebsiteView, self).get_context_data(**kwargs)


        result_slug       = kwargs['result_slug']
        rule_grouping     = kwargs['rule_grouping']
        rule_group_slug   = kwargs['rule_group_slug']
        rule_slug         = kwargs['rule_slug']
        audit_group_slug  = kwargs['audit_group_slug']
        audit_group2_slug = kwargs['audit_group2_slug']
        website_slug      = kwargs['website_slug']

        ar    = AuditResult.objects.get(slug=result_slug)
        wsrr  = WebsiteRuleResult.objects.get(ws_report__audit_result=ar, ws_report__slug=website_slug, slug=rule_slug)
        prrs  = wsrr.page_rule_results.all()

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'


        for prr in prrs:
            prr.href = reverse('rule_group_result_rule_audit_group_audit_group2_website_page', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, audit_group_slug, audit_group2_slug, website_slug, prr.page_result.page_number])

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_audit_groups(audit_group_slug, audit_group2_slug)
        self.result_nav.set_website_page(website_slug)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']        = ar.audit.slug
        context['result_slug']       = result_slug
        context['rule_grouping']     = rule_grouping
        context['rule_group_slug']   = rule_group_slug
        context['rule_slug']         = rule_slug
        context['audit_group_slug']  = audit_group_slug
        context['audit_group2_slug'] = audit_group2_slug
        context['website_slug']      = website_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                    = Rule.objects.get(slug=rule_slug)

        context['website_rule_result']     = wsrr
        context['page_rule_results']       = prrs

        return context

class RuleGroupResultRuleAuditGroupAuditGroup2WebsitePageView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_audit_group_audit_group2_website_page.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleAuditGroupAuditGroup2WebsitePageView, self).get_context_data(**kwargs)


        result_slug       = kwargs['result_slug']
        rule_grouping     = kwargs['rule_grouping']
        rule_group_slug   = kwargs['rule_group_slug']
        rule_slug         = kwargs['rule_slug']
        audit_group2_slug = kwargs['audit_group2_slug']
        website_slug      = kwargs['website_slug']
        page_num          = kwargs['page_num']

        ar   = AuditResult.objects.get(slug=result_slug)
        ag2r = AuditGroup2Result.objects.get(group_result__audit_result=ar, slug=audit_group2_slug)
        wsrr = WebsiteRuleResult.objects.get(ws_report__audit_result=ar, ws_report__slug=website_slug, slug=rule_slug)
        pr   = PageResult.objects.get(ws_report__audit_result=ar, ws_report__slug=website_slug, page_number=page_num)
        prr  = wsrr.page_rule_results.get(page_result__page_number=page_num)

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_audit_groups(None, audit_group2_slug)
        self.result_nav.set_website_page(website_slug, page_num, wsrr.ws_report.page_count)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']        = ar.audit.slug
        context['result_slug']       = result_slug
        context['rule_grouping']     = rule_grouping
        context['rule_group_slug']   = rule_group_slug
        context['rule_slug']         = rule_slug
        context['audit_group2_slug'] = audit_group2_slug
        context['website_slug']      = website_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                 = Rule.objects.get(slug=rule_slug)

        context['audit_group2']         = ag2r
        context['website_rule_result']  = wsrr
        context['page_result']          = pr
        context['page_rule_result']     = prr

        return context


class RuleGroupResultRuleAuditGroup2View(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_audit_group2.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleAuditGroup2View, self).get_context_data(**kwargs)


        result_slug       = kwargs['result_slug']
        rule_grouping     = kwargs['rule_grouping']
        rule_group_slug   = kwargs['rule_group_slug']
        rule_slug         = kwargs['rule_slug']
        audit_group2_slug = kwargs['audit_group2_slug']

        ar  = AuditResult.objects.get(slug=result_slug)
        ag2r = AuditGroup2Result.objects.get(group_result__audit_result=ar, slug=audit_group2_slug)
        ag2rr = ag2r.group2_rule_results.get(slug=rule_slug)

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'


        wsrrs = WebsiteRuleResult.objects.filter(ws_report__audit_result=ar, ws_report__group2_result__slug=audit_group2_slug, slug=rule_slug)
        for wsrr in wsrrs:
            wsrr.title = wsrr.get_title()
            wsrr.href  = reverse('rule_group_result_rule_audit_group2_website', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, audit_group2_slug, wsrr.ws_report.slug])

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_audit_groups(None, audit_group2_slug)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']        = ar.audit.slug
        context['result_slug']       = result_slug
        context['rule_grouping']     = rule_grouping
        context['rule_group_slug']   = rule_group_slug
        context['rule_slug']         = rule_slug
        context['audit_group2_slug'] = audit_group2_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                      = Rule.objects.get(slug=rule_slug)

        context['audit_group2_result']       = ag2r
        context['audit_group2_rule_result']  = ag2rr
        context['website_rule_results']      = wsrrs

        return context

class RuleGroupResultRuleAuditGroup2WebsiteView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_audit_group2_website.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleAuditGroup2WebsiteView, self).get_context_data(**kwargs)


        result_slug       = kwargs['result_slug']
        rule_grouping     = kwargs['rule_grouping']
        rule_group_slug   = kwargs['rule_group_slug']
        rule_slug         = kwargs['rule_slug']
        audit_group2_slug = kwargs['audit_group2_slug']
        website_slug      = kwargs['website_slug']

        ar   = AuditResult.objects.get(slug=result_slug)
        ag2r = AuditGroup2Result.objects.get(group_result__audit_result=ar, slug=audit_group2_slug)
        wsrr = WebsiteRuleResult.objects.get(ws_report__audit_result=ar, ws_report__slug=website_slug, slug=rule_slug)
        prrs = wsrr.page_rule_results.all()

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'


        for prr in prrs:
            prr.href = reverse('rule_group_result_rule_audit_group2_website_page', args=[result_slug, rule_grouping, rule_group_slug, rule_slug, audit_group2_slug, website_slug, prr.page_result.page_number])

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_audit_groups(None, audit_group2_slug)
        self.result_nav.set_website_page(website_slug)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']        = ar.audit.slug
        context['result_slug']       = result_slug
        context['rule_grouping']     = rule_grouping
        context['rule_group_slug']   = rule_group_slug
        context['rule_slug']         = rule_slug
        context['audit_group2_slug'] = audit_group2_slug
        context['website_slug']      = website_slug

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']    = rule_group_label

        context['rule']                    = Rule.objects.get(slug=rule_slug)

        context['audit_group2']            = ag2r
        context['website_rule_result']     = wsrr
        context['page_rule_results']       = prrs

        return context

class RuleGroupResultRuleAuditGroup2WebsitePageView(ResultNavigationMixin, TemplateView):
    template_name = 'ruleResults/rule_group_result_rule_audit_group2_website_page.html'

    def get_context_data(self, **kwargs):
        context = super(RuleGroupResultRuleAuditGroup2WebsitePageView, self).get_context_data(**kwargs)


        result_slug       = kwargs['result_slug']
        rule_grouping     = kwargs['rule_grouping']
        rule_group_slug   = kwargs['rule_group_slug']
        rule_slug         = kwargs['rule_slug']
        audit_group2_slug = kwargs['audit_group2_slug']
        website_slug      = kwargs['website_slug']
        page_num          = kwargs['page_num']

        ar   = AuditResult.objects.get(slug=result_slug)
        ag2r = AuditGroup2Result.objects.get(group_result__audit_result=ar, slug=audit_group2_slug)
        wsrr = WebsiteRuleResult.objects.get(ws_report__audit_result=ar, ws_report__slug=website_slug, slug=rule_slug)
        prr  = wsrr.page_rule_results.get(page_result__page_number=page_num)

        if rule_grouping == 'gl':
            rule_group_label    = Guideline.objects.get(slug=rule_group_slug).title
        else:
            if rule_grouping == 'rs':
                rule_group_label    = RuleScope.objects.get(slug=rule_group_slug).title
            else:
                rule_group_label    = RuleCategory.objects.get(slug=rule_group_slug).title
                rule_grouping    = 'rc'

        # Setup report navigation
        self.result_nav.set_audit_result(ar, 'rules', self.request.path)
        self.result_nav.set_rule_grouping(rule_grouping, rule_group_slug)
        self.result_nav.set_audit_groups(None, audit_group2_slug)
        self.result_nav.set_website_page(website_slug, page_num, wsrr.ws_report.page_count)
        self.result_nav.set_rule(rule_slug)
        self.result_nav.create_result_navigation()

        # slugs used for urls
        context['audit_slug']        = ar.audit.slug
        context['result_slug']       = result_slug
        context['rule_grouping']     = rule_grouping
        context['rule_group_slug']   = rule_group_slug
        context['rule_slug']         = rule_slug
        context['audit_group2_slug'] = audit_group2_slug
        context['website_slug']      = website_slug
        context['page_num']          = page_num

        # objects for rendering content
        context['audit']         = ar.audit
        context['audit_result']  = ar

        context['rule_group_label']     = rule_group_label
        context['audit_group2']         = ag2r
        context['website_rule_result']  = wsrr
        context['page_rule_result']     = prr
        context['rule']                 = Rule.objects.get(slug=rule_slug)


        return context
