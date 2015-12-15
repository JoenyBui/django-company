# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20151103_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(null=True, to='company.Company', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='privilege',
            field=models.IntegerField(choices=[(0, 'Administrated Access'), (1, 'Write Access'), (2, 'View Access'), (3, 'No Access')], default=1),
        ),
    ]
