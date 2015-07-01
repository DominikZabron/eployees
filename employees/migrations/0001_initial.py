# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('middle_name', models.CharField(max_length=200)),
                ('pesel', models.CharField(max_length=11)),
                ('id_number', models.CharField(max_length=9)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200, verbose_name=b'Kod pocztowy')),
                ('country', models.CharField(default=b'Polska', max_length=200, verbose_name=b'Kraj')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
