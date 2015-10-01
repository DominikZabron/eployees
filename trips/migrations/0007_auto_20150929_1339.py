# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_auto_20150929_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstripsettlement',
            name='status',
            field=models.CharField(default=b'i', max_length=1, verbose_name=b'Decyzja', choices=[(b'i', b'Wprowadzanie'), (b'w', b'Oczekuje'), (b'a', b'Rozliczono'), (b'r', b'Odrzucono')]),
        ),
    ]
