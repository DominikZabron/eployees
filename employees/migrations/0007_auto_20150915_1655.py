# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_qualificationsemployee_ordinal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualificationsemployee',
            name='ordinal',
        ),
        migrations.AddField(
            model_name='qualifications',
            name='ordinal',
            field=models.PositiveIntegerField(default=1, verbose_name=b'LP'),
            preserve_default=False,
        ),
    ]
