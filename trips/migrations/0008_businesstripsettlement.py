# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_businesstripitem_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTripSettlement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_trip_item', models.ForeignKey(verbose_name=b'Wyjazd s\xc5\x82u\xc5\xbcbowy', to='trips.BusinessTripItem')),
            ],
            options={
                'verbose_name': 'Rozliczenie',
                'verbose_name_plural': 'Rozliczenia',
            },
        ),
    ]
