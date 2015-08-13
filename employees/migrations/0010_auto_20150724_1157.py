# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_auto_20150702_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(max_length=200, verbose_name=b'Miejscowo\xc5\x9b\xc4\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(max_length=200, verbose_name=b'Drugie imi\xc4\x99', blank=True),
        ),
    ]
