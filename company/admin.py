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