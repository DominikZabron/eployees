# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0019_auto_20150827_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesstripinvoicemilage',
            name='amount',
        ),
    ]
