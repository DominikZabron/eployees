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
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Nazwa pojazdu')),
                ('brand', models.CharField(max_length=200, verbose_name=b'Marka pojazdu')),
                ('registration_number', models.CharField(max_length=200, verbose_name=b'Numer rejestracyjny')),
                ('engine_capacity', models.IntegerField(max_length=200, verbose_name=b'Pojemnosc silnika')),
                ('is_company_owned', models.BooleanField(max_length=200, verbose_name=b'Wlasnosc firmy')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
