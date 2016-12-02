
from django.contrib import admin
from company.models import Company, Employee


class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('public_id', 'user', 'privilege', 'company')


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 3


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'public_id', 'street', 'city', 'state', 'zipcode')
    fieldsets = [
        (
            None, {
                'fields': ('name', 'street', 'city', 'state', 'zipcode')
            }
        ),
    ]
    inlines = [EmployeeInline]


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeProfileAdmin)