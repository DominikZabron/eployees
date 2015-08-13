# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_businesstripsettlement'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstripsettlement',
            name='costs_all',
            field=models.DecimalField(default=0, verbose_name=b'\xc5\x81\xc4\x85czne koszty do rozliczenia', max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesstripsettlement',
            name='description',
            field=models.TextField(verbose_name=b'Opis', blank=True),
        ),
    ]
