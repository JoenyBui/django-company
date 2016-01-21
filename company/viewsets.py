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

from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions

from .models import Company, Employee
from .serializer import UserSerializer, CompanySerializer, EmployeeSerializer


__author__ = 'jbui'


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )
    # filter_fields = ('first_name', 'last_name', 'date_joined')


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Company API viewset.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated, )

    # def get_queryset(self):
    #     user = self.request.user
    #
    #     return Employee.objects.filter(user=user)[0].company


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Employee API viewset.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user

        return Employee.objects.filter(user=user)[0].company.employee_set.all()
