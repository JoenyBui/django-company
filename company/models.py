import os
import sys
import datetime
import json
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.conf import settings

from rest_framework.authtoken.models import Token

from mptt.models import MPTTModel

from . import USER_PRIVELAGE, USER_NONE, USER_COMPANY_ADMIN, USER_READONLY, USER_WORKER

# Create your models here.


class Company(models.Model):
    """
    Company Registration Model
    """
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    street = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=10, default='')
    zipcode = models.IntegerField(default=0)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return "Company Name: %s | Street: %s | City: %s | State: %s | Zipcode: %d" % \
               (self.name, self.street, self.city, self.state, self.zipcode)

    def add_employee(self, username, token):
        """
        The Company administrator will add the employee given a username and their unique token.
        :param username:
        :param token:
        """
        user = User.objects.get(username=username)

        if user.auth_token.key == token:
            Employee.objects.create(company=self, user=user)

    def remove_employee(self, username):
        """

        :param username:
        """
        user = User.objects.get(username=username)

        if user:
            employee = self.employee_set.get(user=user)

            if employee:
                # If there is an employee.
                employee.delete()

    def change_employee_privilege(self, username, privilege):
        """
        Change employee privilege
        :param username:
        :param privilege:
        """
        user = User.objects.get(username=username)

        if user:
            employee = self.employee_set.get(user=user)

            if employee:
                # Change the user privilege.
                employee.privilege = privilege


class Employee(models.Model):
    """
    Employee

    Employee can only be created through the company profile page.  Once the temporary
    employee profile is created, the employee must activate it before it can be used.

    Privilege is given to the user through the company administrative.
    """
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    privilege = models.IntegerField(default=1, choices=USER_PRIVELAGE)

    def __str__(self):
        return self.company.name + " " + self.user.username

    def accept_company(self):
        """
        Accept company invitation.
        :return:
        """
        pass

    def request_privilege(self):
        """
        Request new privilege.
        :return:
        """
        pass


def get_user_company(user):
    """
    Get the company of the user if give one.

    :param user:
    :return:
    """
    if user.employee_set.all():
        # User is an employee.
        if Employee.objects.get(user=user):
            employee = Employee.objects.get(user=user)

            return employee.company
        else:
            return None
    else:
        return None
