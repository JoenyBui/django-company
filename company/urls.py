"""
 *  PROTECTION ENGINEERING CONSULTANTS CONFIDENTIAL
 *
 *  [2014] - [2015] Protection Engineering Consultants
 *  All Rights Reserved.
 *
 * NOTICE:  All information contained herein is, and remains
 * the property of Protection Engineering Consultants and its suppliers,
 * if any.  The intellectual and technical concepts contained
 * herein are proprietary to Protection Engineering Consultants
 * and its suppliers and may be covered by U.S. and Foreign Patents,
 * patents in process, and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material
 * is strictly forbidden unless prior written permission is obtained
 * from Protection Engineering Consultants.
"""

from django.conf.urls import url
from django.conf.urls import patterns
from django.conf.urls import include
from django.views.generic.base import TemplateView

from .views import ProfileView, CompanyView, EmployeeCreateView

__author__ = 'jbui'

urlpatterns = patterns('',
    url(r'^profile/$', ProfileView.as_view(), name="profile"),
    url(r'^company/$', CompanyView.as_view(), name="company"),
    url(r'^employee/$', EmployeeCreateView.as_view(), name='employee'),
)