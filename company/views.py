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

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from django.views.generic.edit import FormView, UpdateView, CreateView, View
from django.http import HttpResponseRedirect

from rest_framework.authtoken.models import Token

from .models import Company

from .forms import UserForm, EmployeeForm, CompanyForm
from .forms import EmployeeFormSet

__author__ = 'jbui'


class ProfileView(View):
    """
    User Profile Information.
    """

    def get(self, request):
        """

        :param request:
        :return:
        """
        user = User.objects.get(pk=request.user.id)

        # Look to see if employee information exists, otherwise redirect to ask administration
        # to add user.
        if user.employee_set.exists():

            employee = user.employee_set.get()

            form = UserForm(instance=user)

            form.fields['username'].widget.attrs['disabled'] = True

            token = Token.objects.get_or_create(user=user)

            return render(request, 'administration/profile.html',
                {
                    'username': str(user),
                    'form': form,
                    'token': token[0],
                    'privilege': USER_PRIVELAGE[employee.privilege][1]
                })
        else:
            return render(request,
                          "error.html",
                          {
                              'username': str(user),
                              'error_title': 'Not Employed',
                              'error_summary': ERROR_LOG['Not Employed']
                          })

    def post(self, request):
        """

        :param request:
        :return:
        """
        user = User.objects.get(pk=request.user.id)
        if user.employee_set.exists():

            employee = user.employee_set.get()

            form = UserForm(data=request.POST, instance=user)

            # If data is valid, proceeds to update the new post.
            if form.is_valid():
                form.save()

                # Redirect after POST
                return HttpResponseRedirect('/thanks/')
            else:
                return render(request,
                              'administration/profile.html',
                              {
                                  'username': str(user),
                                  'form': form,
                                  'privilege': USER_PRIVELAGE[employee.privilege][1]
                              })
        else:
            return render(request,
                          "error.html",
                          {
                              'username': str(user),
                              'error_title': 'Not Employed',
                              'error_summary': ERROR_LOG['Not Employed']
                          })


class CompanyView(View):
    """
    Company view.
    """

    def get(self, request):
        """

        :param request:
        :return:
        """
        user = User.objects.get(pk=request.user.id)

        if user.employee_set.exists():
            employee = user.employee_set.get()
            company = employee.company

            form = CompanyForm(instance=company)

            if employee.privilege != 0:
                form.fields['name'].widget.attrs['disabled'] = True
                form.fields['street'].widget.attrs['disabled'] = True
                form.fields['city'].widget.attrs['disabled'] = True
                form.fields['state'].widget.attrs['disabled'] = True
                form.fields['zipcode'].widget.attrs['disabled'] = True
                form.fields['website'].widget.attrs['disabled'] = True
                form.fields['picture'].widget.attrs['disabled'] = True

            return render(request,
                          'administration/company.html',
                          {
                              'username': str(user),
                              'form': form,
                              'employee': employee,
                              'privilege': USER_PRIVELAGE[employee.privilege][1]
                          })
        else:
            return render(request,
                          "error.html",
                          {
                              'username': str(user),
                              'error_title': 'Not Employed',
                              'error_summary': ERROR_LOG['Not Employed']
                          })

    def post(self, request):
        """
        Submit the administration.
        :param request:
        :return:
        """
        user = User.objects.get(pk=request.user.id)

        if user.employee_set.exists():
            employee = user.employee_set.get()
            company = employee.company

            form = CompanyForm(request.POST or None, instance=company)

            # check whether it's valid.
            if form.is_valid():
                form.save()

                return HttpResponseRedirect('/thanks/')
            else:
                return render(request,
                          'administration/company.html',
                          {
                              'username': str(user),
                              'form': form,
                              'employee': employee,
                              'privilege': USER_PRIVELAGE[employee.privilege][1]
                          })
        else:
            return render(request,
                          "error.html",
                          {
                              'username': str(user),
                              'error_title': 'Not Employed',
                              'error_summary': ERROR_LOG['Not Employed']
                          })


class EmployeeCreateView(CreateView):
    """
    Create a new employee.
    """

    template_name = 'administration/employee.html'
    model = Company
    form_class = EmployeeForm
    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        employee_set = EmployeeFormSet
        return self.render_to_response(
            self.get_context_data(form=form,
                                  employee_set=employee_set))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        employee_set = EmployeeFormSet(self.request.POST)

        if (form.is_valid() and employee_set.is_valid()):
            return self.form_valid(form, employee_set)
        else:
            return self.form_invalid(form, employee_set)

    def form_valid(self, form, employee_set):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()

        employee_set.instance = self.object
        employee_set.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, employee_set):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  employee_set=employee_set))
