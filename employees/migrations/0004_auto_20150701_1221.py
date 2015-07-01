# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20150701_1120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'dane dodatkowe', 'verbose_name_plural': 'dane dodatkowe'},
        ),
    ]
