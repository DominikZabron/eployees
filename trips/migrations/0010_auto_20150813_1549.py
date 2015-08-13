# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0009_auto_20150813_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstripsettlement',
            name='status',
            field=models.CharField(default=b'w', max_length=1, verbose_name=b'Decyzja', choices=[(b'w', b'Oczekuje'), (b'a', b'Zaakceptowany'), (b'r', b'Odrzucony')]),
        ),
        migrations.AlterField(
            model_name='businesstripitem',
            name='status',
            field=models.CharField(default=b'w', max_length=1, verbose_name=b'Decyzja', choices=[(b'w', b'Oczekuje'), (b'a', b'Zaakceptowany'), (b'r', b'Odrzucony')]),
        ),
    ]
