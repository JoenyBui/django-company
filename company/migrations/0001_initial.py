# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=100, default='')),
                ('city', models.CharField(max_length=100, default='')),
                ('state', models.CharField(max_length=10, default='')),
                ('zipcode', models.IntegerField(default=0)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to='profile_images', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('privilege', models.IntegerField(choices=[(0, 'Administrated Access'), (1, 'Write Access'), (2, 'View Access'), (3, 'No Access')], default=1)),
                ('company', models.ForeignKey(default=False, to='company.Company')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
