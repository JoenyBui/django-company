from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..company.models import Company, Employee


class CompanyTests(APITestCase):
    """

    """
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('wam')
        data = {'public id': '', 'folder_id': '', 'name': 'new_entry', 'data': ''}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().name, 'DabApps')


class EmployeeTests(APITestCase):
    """

    """
    def test_create_account(self):

        pass