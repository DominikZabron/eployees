# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0011_businesstripitem_pojazd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businesstripitem',
            old_name='pojazd',
            new_name='vehicle',
        ),
        migrations.AddField(
            model_name='businesstripitem',
            name='distance',
            field=models.IntegerField(default=0, verbose_name=b'Odleg\xc5\x82o\xc5\x9b\xc4\x87 [km]'),
            preserve_default=False,
        ),
    ]
