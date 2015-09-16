# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20150907_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'nazwa')),
            ],
            options={
                'verbose_name': 'uprawnienie',
                'verbose_name_plural': 'uprawnienia',
            },
        ),
        migrations.CreateModel(
            name='QualificationsEmployee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expiry_date', models.DateField(verbose_name=b'wygasaj\xc4\x85')),
                ('employee', models.ForeignKey(verbose_name=b'pracownik', to='employees.Employee')),
                ('qualifications', models.ForeignKey(verbose_name=b'uprawnienia', to='employees.Qualifications')),
            ],
            options={
                'verbose_name': 'uprawnienie',
                'verbose_name_plural': 'uprawnienia',
            },
        ),
    ]
