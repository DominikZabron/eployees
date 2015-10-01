# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_auto_20150929_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businesstriproute',
            old_name='trip',
            new_name='settlement',
        ),
    ]
