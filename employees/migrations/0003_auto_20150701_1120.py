# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20150701_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(max_length=200, verbose_name=b'Drugie imie'),
        ),
    ]
