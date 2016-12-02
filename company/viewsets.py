
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
