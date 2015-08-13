# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20150707_1434'),
        ('trips', '0010_auto_20150813_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstripitem',
            name='pojazd',
            field=models.ForeignKey(default=1, verbose_name=b'Pojazd', to='assets.Car'),
            preserve_default=False,
        ),
    ]
