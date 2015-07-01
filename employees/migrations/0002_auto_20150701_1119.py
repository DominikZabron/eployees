# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'lista pracownikow', 'verbose_name_plural': 'lista pracownikow'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(max_length=200, verbose_name=b'Miejscowosc'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id_number',
            field=models.CharField(max_length=9, verbose_name=b'Nr dowodu'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(max_length=200, verbose_name=b'Pesel'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pesel',
            field=models.CharField(max_length=11, verbose_name=b'Pesel'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='street',
            field=models.CharField(max_length=200, verbose_name=b'Adres'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
