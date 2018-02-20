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

file: websiteResults/views.py

Author: Jon Gunderson

"""

from __future__ import absolute_import
from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import redirect

from django.contrib import messages

from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import RedirectView

from django.contrib.auth.models import User

from auditResults.models       import AuditResult
from auditGroupResults.models  import AuditGroupResult
from auditGroup2Results.models import AuditGroup2Result

from websiteResults.models     import WebsiteResult
from websiteResults.models     import WebsiteGuidelineResult
from websiteResults.models     import WebsiteRuleScopeResult
from websiteResults.models     import WebsiteRuleCategoryResult

from pageResults.models    import PageRuleCategoryResult
from pageResults.models    import PageGuidelineResult
from pageResults.models    import PageRuleScopeResult
from rulesets.models       import Ruleset
from userProfiles.models   import UserProfile

from ruleCategories.models import RuleCategory
from wcag20.models         import Guideline
from rules.models          import RuleScope
from contacts.models       import Announcement


from itertools import chain

from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from audits.uid import generate

# ==============================================================
#
# FAE Auditor Result Navigation Mixin
#
# ==============================================================

class UrlItem:

    def __init__(self, label, url):
        self.label = label
        self.url   = url

class UrlItems:

    items = []

    def __init__(self, label):
        self.label = label
        self.items = []

    def add(self, label, url):
        self.items.append(UrlItem(label, url))

    def set_label(self, label):
        self.label = label

    def remove_all(self):
        self.items = []

    def item_count(self):
        return len(self.items)

class ResultNavigtionObject:

    view_options = UrlItems('')
    filters      = UrlItems('')

    def __init__(self, session, user=False):

        self.session = session

        a = None
        ar = None

        try:
            self.audit_slug = self.session['audit_slug']

            a = Audit.objects.get(slug=audit_slug)

            try:
                self.audit_result_slug = self.session['audit_result_slug']
                ar = AuditResult.objects.get(audit=a, slug=self.audit_result_slug)
            except:
                try:
                    ar = a.audit_results().last()
                except:
                    ar = None

            try:
                self.result_view = self.session['result_view']
            except:
                self.result_view = 'rules'

            try:
                self.audit_group_slug = self.session['audit_group_slug']
            except:
                self.audit_group_slug = ''

            try:
                self.audit_group2_slug = self.session['audit_group2_slug']
            except:
                self.audit_group2_slug = ''

            try:
                self.rule_grouping = self.session['rule_grouping']
            except:
                self.rule_grouping = 'rc'

            try:
                self.rule_group = self.session['rule_group']
            except:
                self.rule_group = ''

            try:
                self.rule_slug = self.session['rule_slug']
            except:
                self.rule_slug = ''

            try:
                self.website_slug = self.session['website_slug']
            except:
                self.website_slug = ''

            try:
                self.page_num = self.session['page_num']
            except:
                self.page_num = ''

            try:
                self.page_count = self.session['page_count']
            except:
                self.page_count = ''

        except:
            self.audit_slug        = False
            self.audit_result_slug = ''
            self.result_view       = 'rules'

            self.audit_group_slug = ''
            self.audit_group2_slug = ''

            self.rule_grouping = 'rc'
            self.rule_group = ''
            self.rule_slug = ''

            self.website_slug = ''
            self.page_num = ''
            self.page_count = 0

        if ar:
            this.create_result_navigation()

    def create_result_navigation(self):
        self.create_view_options()
        self.create_filters()


    def set_audit_result(self, audit_slug, audit_result_slug, result_view):

        if audit_slug:
          self.audit_slug            = audit_slug
          self.session['audit_slug'] = audit_slug

        if audit_result_slug:
          self.audit_result_slug            = audit_result_slug
          self.session['audit_result_slug'] = audit_result_slug

        if result_view:
          self.result_view            = result_view
          self.session['result_view'] = result_view

        # Reset group information
        self.audit_group_slug = ''
        self.session['audit_group_slug'] = self.audit_group_slug

        self.audit_group2_slug = ''
        self.session['audit_group2_slug'] = self.audit_group2_slug

        # Reset rule information
        self.rule_grouping = 'rc'
        self.session['rule_grouping'] = self.rule_grouping

        self.rule_group = ''
        self.session['rule_group'] = self.rule_group

        self.rule_slug = ''
        self.session['rule_slug'] = self.rule_slug

        # Reset website/page information
        self.website_slug = ''
        self.session['website_slug'] = self.website_slug

        self.page_num = ''
        self.session['page_num'] = self.page_num

        self.page_count = 0
        self.session['page_count'] = self.page_count


    def set_audit_group(self, audit_group_slug, audit_group2_slug):

        if audit_group_slug:
          self.audit_group_slug            = audit_group_slug
          self.session['audit_group_slug'] = audit_group_slug

        if audit_group2_slug:
          self.audit_group2_slug            = audit_group2_slug
          self.session['audit_group2_slug'] = audit_group2_slug

    def set_rule_grouping(self, rule_grouping, rule_group=None):

        if rule_grouping:
          self.rule_grouping = rule_grouping
          self.session['rule_grouping'] = rule_grouping

        if rule_group:
          self.rule_group = rule_group
          self.session['rule_group'] = rule_group


    def set_rule(self, rule_slug):

        if rule_slug:
          self.rule_slug = rule_slug
          self.session['rule_slug'] = rule_slug

    def set_website_page(self, website_slug=None, page_num=None, page_count=None):

        if website_slug:
          self.website_slug = website_slug
          self.session['website_slug'] = website_slug

        if page_num:
          self.page_num = page_num
          self.session['page_num'] = page_num

        if page_count:
          self.page_count = page_count
          self.session['page_count'] = page_count


# ---------------------
# View options
# ---------------------

    def view_option_audit_result(self):
        self.view_options.add('Rule Category', reverse('audit_result', args=[self.audit_result_slug, 'rc']))
        self.view_options.add('Guidelines',    reverse('audit_result', args=[self.audit_result_slug, 'gl']))
        self.view_options.add('Rule Scope',    reverse('audit_result', args=[self.audit_result_slug, 'rs']))

    def view_option_website_results(self):
        self.view_options.add('Rule Category', reverse('website_results', args=[self.audit_result_slug, 'rc']))
        self.view_options.add('Guidelines',    reverse('website_results', args=[self.audit_result_slug, 'gl']))
        self.view_options.add('Rule Scope',    reverse('website_results', args=[self.audit_result_slug, 'rs']))

    def view_option_website_results_website(self):
        self.view_options.add('Rule Category', reverse('website_results_website', args=[self.audit_result_slug, 'rc', self.website_slug]))
        self.view_options.add('Guidelines',    reverse('website_results_website', args=[self.audit_result_slug, 'gl', self.website_slug]))
        self.view_options.add('Rule Scope',    reverse('website_results_website', args=[self.audit_result_slug, 'rs', self.website_slug]))

    def view_option_website_results_website_page(self):
        self.view_options.add('Rule Category', reverse('website_results_website_page', args=[self.audit_result_slug, 'rc', self.website_slug, self.page_num]))
        self.view_options.add('Guidelines',    reverse('website_results_website_page', args=[self.audit_result_slug, 'gl', self.website_slug, self.page_num]))
        self.view_options.add('Rule Scope',    reverse('website_results_website_page', args=[self.audit_result_slug, 'rs', self.website_slug, self.page_num]))

    def view_option_website_results_website_page_rule(self):
        self.view_options.add('Rule Category', reverse('website_results_website_page_rule', args=[self.audit_result_slug, 'rc', self.website_slug, self.page_num, self.rule_slug]))
        self.view_options.add('Guidelines',    reverse('website_results_website_page_rule', args=[self.audit_result_slug, 'gl', self.website_slug, self.page_num, self.rule_slug]))
        self.view_options.add('Rule Scope',    reverse('', args=[self.audit_result_slug, 'rs', self.website_slug, self.page_num, self.rule_slug]))

    def create_view_options(self):

        self.view_options.remove_all()

        if self.result_view == 'rules':
            self.view_option_audit_result()
        # Assume 'website' result view
        else:

            if self.audit_group_slug == '' and self.audit_group2_slug == '':

                if self.rule_slug:
                    self.view_option_website_results_website_page_rule()
                    return

                if self.page_num:
                    self.view_option_website_results_website_page()
                    return

                if self.website_slug:
                    self.view_option_website_results_website()
                    return

                self.view_option_website_results()
                return
# ---------------------
# Rule Grouping Filters
# ---------------------

    def filter_website_results(self, group, label):
        if group:
            return reverse('website_rule_group_results', args=[self.audit_result_slug, self.rule_grouping, group])
        else:
            return reverse('website_results', args=[self.audit_result_slug, self.rule_grouping])

    def filter_website_results_website(self, group, label):
        if group:
            return reverse('website_rule_group_results_website', args=[self.audit_result_slug, self.rule_grouping, group, self.website_slug])
        else:
            return reverse('website_results_website', args=[self.audit_result_slug, self.rule_grouping, self.website_slug])

    def filter_website_results_website_page(self, group, label):
        if group:
            return reverse('website_rule_group_results_website_page', args=[self.audit_result_slug, self.rule_grouping, group, self.website_slug, self.page_num])
        else:
            return reverse('website_results_website_page', args=[self.audit_result_slug, self.rule_grouping, self.website_slug, self.page_num])

    def filter_audit_result(self, group, label):
        if group:
            return reverse('audit_result_rule_group', args=[self.result_slug, self.rule_grouping, group])
        else:
            return reverse('audit_result', args=[self.result_slug, self.rule_grouping])


    def add_filter_item(self, group, label):

        if self.result_view == 'rules':
            self.filter_audit_result(group, label)
        # Assume 'website' result view
        else:

            if self.audit_group_slug == '' and self.audit_group2_slug == '':

                if self.page_num:
                    url = self.filter_website_results_website_page(group, label)
                else:
                    if self.website_slug:
                        url = self.filter_website_results_website(group, label)
                    else:
                        url = self.filter_website_results(group, label)

        self.filters.add(label, url)

    def add_rule_category_filter(self):
        rcs = RuleCategory.objects.all()
        self.add_filter_item(False, "All Groups")
        for rc in rcs:
            self.add_filter_item(rc.slug, rc.title)

    def add_guideline_filter(self):
        gls = Guideline.objects.all()
        self.add_filter_item(False, "All Groups")
        for gl in gls:
            self.add_filter_item(gl.slug, gl.title)

    def add_rule_scope_filter(self):
        rss = RuleScope.objects.all()
        self.add_filter_item(False, "All Groups")
        for rs in rss:
            self.add_filter_item(rs.slug, rs.title)

    def create_filters(self):

        self.filters.remove_all()

        if self.rule_grouping == 'rs':
            self.filters.set_label('Rule Scope')
            self.add_rule_scope_filter()
        elif self.rule_grouping == 'gl':
            self.filters.set_label('Guidlines')
            self.add_guideline_filter()
        else:
            self.filters.set_label('Rule Categories')
            self.add_rule_category_filter()

class ResultNavigationMixin:


    def get_context_data(self, **kwargs):

        context = super(ResultNavigationMixin, self).get_context_data(**kwargs)

        self.result_nav = ResultNavigtionObject(self.request.session, self.request.user)

        context['result_nav'] = self.result_nav

        return context


