# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20150729_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesstrip',
            options={'verbose_name': 'Delegacja', 'verbose_name_plural': 'Delegacje'},
        ),
    ]
