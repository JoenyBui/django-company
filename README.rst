=====
Company
=====

Company is a Django app that organizes a company/employee module.  It is used to help the
user organize their files.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "company" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'company',
    )

2. Include the company URLconf in your project urls.py like this::

    url(r'^company/', include('company.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a folder_tree (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/company/ to participate in the poll.