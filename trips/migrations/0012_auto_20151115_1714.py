# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import trips.models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0011_auto_20151113_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstripinvoicefare',
            name='scan',
            field=models.ImageField(upload_to=trips.models.file_name),
        ),
    ]
