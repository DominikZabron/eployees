# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import trips.models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0009_auto_20150930_1526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesstripallowance',
            options={'ordering': ['begin_time'], 'verbose_name': 'Dieta', 'verbose_name_plural': 'Diety'},
        ),
        migrations.AddField(
            model_name='businesstripinvoicefare',
            name='scan',
            field=models.ImageField(upload_to=trips.models.file_name, blank=True),
        ),
    ]
