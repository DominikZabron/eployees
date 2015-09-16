# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_auto_20150915_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='health_safety_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='medical_check_date',
        ),
    ]
