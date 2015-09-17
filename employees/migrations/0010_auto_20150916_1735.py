# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0009_auto_20150916_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualificationsemployee',
            name='qualifications',
            field=models.ForeignKey(verbose_name=b'uprawnienia', to='employees.Qualifications'),
        ),
    ]
