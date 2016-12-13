from django.apps import AppConfig


class CompanyConfig(AppConfig):
    name = 'company'
    verbose_name = 'Company/Employee/Permissions'

    def ready(self):
        from . import signals
