# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20150922_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesstripsettlement',
            name='trip',
        ),
        migrations.AddField(
            model_name='businesstripsettlement',
            name='trip_employee',
            field=models.OneToOneField(related_name='settlement', default=1, verbose_name=b'Wyjazd', to='trips.BusinessTripEmployee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='businesstripemployee',
            name='employee',
            field=models.ForeignKey(verbose_name=b'Pracownik', to=settings.AUTH_USER_MODEL),
        ),
    ]
