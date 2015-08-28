# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(parent_link=True, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(max_length=255, verbose_name=b'Stanowisko', blank=True)),
                ('middle_name', models.CharField(max_length=200, verbose_name=b'Drugie imi\xc4\x99', blank=True)),
                ('pesel', models.CharField(max_length=11, verbose_name=b'Pesel', blank=True)),
                ('id_number', models.CharField(max_length=9, verbose_name=b'Nr dowodu', blank=True)),
                ('street', models.CharField(max_length=200, verbose_name=b'Adres', blank=True)),
                ('city', models.CharField(max_length=200, verbose_name=b'Miejscowo\xc5\x9b\xc4\x87', blank=True)),
                ('postcode', models.CharField(max_length=200, verbose_name=b'Kod pocztowy', blank=True)),
                ('country', models.CharField(default=b'Polska', max_length=200, verbose_name=b'Kraj', blank=True)),
                ('medical_check_date', models.DateField(null=True, verbose_name=b'Data wa\xc5\xbcno\xc5\x9bci badania lekarskiego', blank=True)),
                ('health_safety_date', models.DateField(null=True, verbose_name=b'Data wa\xc5\xbcno\xc5\x9bci szkolenia BHP', blank=True)),
            ],
            options={
                'verbose_name': 'dane pracownika',
                'verbose_name_plural': 'dane osobowe',
            },
        ),
    ]
