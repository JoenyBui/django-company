# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20151106_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='state',
            field=models.CharField(max_length=10, default=''),
        ),
    ]
