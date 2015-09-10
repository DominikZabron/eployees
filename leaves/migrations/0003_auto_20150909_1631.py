# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0002_leaverequest_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='available_days',
            field=models.IntegerField(default=26, verbose_name=b'dni urlopu kalendarzowego'),
        ),
    ]
