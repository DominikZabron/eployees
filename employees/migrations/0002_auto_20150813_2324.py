# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='health_safety_date',
            field=models.DateField(null=True, verbose_name=b'Data wa\xc5\xbcno\xc5\x9bci szkolenia BHP', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='medical_check_date',
            field=models.DateField(null=True, verbose_name=b'Data wa\xc5\xbcno\xc5\x9bci badania lekarskiego', blank=True),
        ),
    ]
