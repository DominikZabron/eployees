# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0005_auto_20150716_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='leave',
            field=models.ForeignKey(verbose_name=b'Pracownik', to='leaves.Leave'),
        ),
    ]
