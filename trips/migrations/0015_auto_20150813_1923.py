# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0014_businesstrip_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesstripsettlement',
            name='business_trip_item',
        ),
        migrations.AddField(
            model_name='businesstripsettlement',
            name='business_trip',
            field=models.ForeignKey(default=1, verbose_name=b'Delegacja', to='trips.BusinessTrip'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='businesstripitem',
            name='estimated_cost',
            field=models.DecimalField(verbose_name=b'Szacunkowy koszt [z\xc5\x82]', max_digits=9, decimal_places=2),
        ),
    ]
