
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