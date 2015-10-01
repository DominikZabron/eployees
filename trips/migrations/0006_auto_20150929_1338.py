# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20150923_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstriproute',
            name='trip',
            field=models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripSettlement'),
        ),
        migrations.AlterField(
            model_name='businesstripsettlement',
            name='status',
            field=models.CharField(default=b'w', max_length=1, verbose_name=b'Decyzja', choices=[(b'i', b'Wprowadzanie'), (b'w', b'Oczekuje'), (b'a', b'Rozliczono'), (b'r', b'Odrzucono')]),
        ),
    ]
