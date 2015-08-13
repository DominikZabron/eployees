# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20150729_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstripitem',
            name='business_trip',
            field=models.ForeignKey(default=1, verbose_name=b'Delegacja', to='trips.BusinessTrip'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='businesstripitem',
            name='employee',
            field=models.ForeignKey(verbose_name=b'Pracownik', to=settings.AUTH_USER_MODEL),
        ),
    ]
