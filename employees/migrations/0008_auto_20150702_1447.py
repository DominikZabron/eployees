# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20150702_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Miejscowosc'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='country',
            field=models.CharField(default=b'Polska', max_length=200, null=True, verbose_name=b'Kraj'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id_number',
            field=models.CharField(max_length=9, null=True, verbose_name=b'Nr dowodu'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Drugie imie', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pesel',
            field=models.CharField(max_length=11, null=True, verbose_name=b'Pesel'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='postcode',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='street',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Adres'),
        ),
    ]
