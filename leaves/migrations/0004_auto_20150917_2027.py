# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0003_auto_20150909_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='year',
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='start_date',
            field=models.DateField(verbose_name=b'pocz\xc4\x85tek urlopu'),
        ),
    ]
