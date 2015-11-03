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

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from company.viewsets import UserViewSet, CompanyViewSet, EmployeeViewSet

__author__ = 'jbui'

router = DefaultRouter()
router.register(r'users', UserViewSet, 'user-api')
router.register(r'employee', EmployeeViewSet)
router.register(r'company', CompanyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
