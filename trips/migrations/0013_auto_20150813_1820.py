# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0012_auto_20150813_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstripitem',
            name='vehicle',
            field=models.ForeignKey(verbose_name=b'Pojazd', blank=True, to='assets.Car', null=True),
        ),
    ]
