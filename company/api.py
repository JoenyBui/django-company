
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from company.viewsets import UserViewSet, CompanyViewSet, EmployeeViewSet

__author__ = 'joeny'

router = DefaultRouter()
router.register(r'users', UserViewSet, 'user-api')
router.register(r'employee', EmployeeViewSet)
router.register(r'company', CompanyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
