# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='public_id',
            field=models.UUIDField(editable=False, default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='employee',
            name='public_id',
            field=models.UUIDField(editable=False, default=uuid.uuid4),
        ),
    ]
