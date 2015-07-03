# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine_capacity',
            field=models.IntegerField(verbose_name=b'Pojemnosc silnika'),
        ),
    ]
