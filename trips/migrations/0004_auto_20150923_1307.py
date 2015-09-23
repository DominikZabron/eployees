# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20150922_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesstrip',
            options={'ordering': ['-begin_date'], 'verbose_name': 'Delegacja', 'verbose_name_plural': 'Delegacje'},
        ),
        migrations.AlterUniqueTogether(
            name='businesstripemployee',
            unique_together=set([('employee', 'business_trip')]),
        ),
    ]
