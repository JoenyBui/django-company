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

import smtplib

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from django.conf import settings
from django.core.mail import send_mail, mail_admins, EmailMessage

from .models import Company, Employee
from .models import get_user_company

__author__ = 'jbui'


class CompanyTestCase(TestCase):
    """
    Company Test Case
    """
    def setUp(self):
        self.u1 = User.objects.create_user(username='test1', password='password')
        self.u2 = User.objects.create_user(username='test2', password='password')
        self.u3 = User.objects.create_user(username='test3', password='password')
        self.u4 = User.objects.create_user(username='test4', password='password')

        self.c1 = Company.objects.create(name='Company 1')
        self.c2 = Company.objects.create(name='Company 2')

        self.e1 = Employee.objects.create(user=self.u1, company=self.c1)
        self.e2 = Employee.objects.create(user=self.u2, company=self.c2)
        self.e3 = Employee.objects.create(user=self.u3)

    def test_address(self):
        self.c1.street = '3401 S. Lamar Blvd'
        self.c1.city = 'Austin'
        self.c1.state = 'TX'
        self.c1.zipcode = 78704

        self.assertIsNotNone(self.c1)

    def test_add_employee(self):
        self.c1.add_employee(self.u1.username, self.u1.auth_token.key)
        self.c1.add_employee(self.u2.username, self.u2.auth_token.key)
        self.c2.add_employee(self.u3.username, self.u3.auth_token.key)

        self.assertEqual(len(self.c1.employee_set.all()), 2)

    def test_remove_employee(self):
        self.c1.add_employee(self.u1.username, self.u1.auth_token.key)
        self.assertEqual(len(self.c1.employee_set.all()), 1)

        self.c1.remove_employee(username='test1')
        self.assertEqual(len(self.c1.employee_set.all()), 0)

    def test_user_company(self):
        self.assertEqual(get_user_company(self.u1), self.c1)
        self.assertEqual(get_user_company(self.u2), self.c2)
        self.assertEqual(get_user_company(self.u3), None)
        self.assertEqual(get_user_company(self.u4), None)

    def test_change_employee_privilege(self):
        pass


class EmployeeTestCase(TestCase):
    """
    Employee test case.
    """
    def setUp(self):
        self.e1 = Employee.objects.create()
        pass

    def test_accept_company(self):
        pass


class EmailTestCase(TestCase):
    """

    """
    def setUp(self):
        pass

    def test_email_message(self):
        subject = 'Subject here'
        message = 'Here is the message'
        email = 'joeny.bui@gmail.com'

        mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
        # mail.attach(attach.name, attach.read(), attach.content_type)
        mail.send()

    def test_email(self):
        sender = settings.DEFAULT_FROM_EMAIL
        recipients = ['joeny.bui@gmail.com']

        self.assertTrue(
            send_mail('Subject here', 'Here is the message.',
                      sender, recipients, fail_silently=False)
        )

        self.assertTrue(send_mail('Subject here', 'Here is the message.',
                                  'ralberson@protection-consultants.com', recipients, fail_silently=False))

    def test_smtp(self):
        # server = 'intranet.protection-consultants.com'
        server = '10.71.62.9'
        # recipients = ['jbui@protection-consultants.com']

        recipients = ['joeny.bui@gmail.com']
        # sender = 'ralberson@protection-consultants.com'
        sender = 'support@protection-consultants.com'
        message = """
        Subject: SMTP e-mail test

        This is a test e-mail message.
        """

        session = smtplib.SMTP(server, 25)
        session.ehlo()
        session.starttls()
        session.ehlo()
        print(session.login(user='support', password='Protection2015!'))

        self.assertTrue(session.sendmail(sender, recipients, message))

        session.close()