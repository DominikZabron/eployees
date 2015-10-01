# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20150923_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstripemployee',
            name='begin_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 23, 15, 46, 59, 274984), verbose_name=b'Data pocz\xc4\x85tkowa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesstripemployee',
            name='description',
            field=models.TextField(verbose_name=b'Uzasadnienie', blank=True),
        ),
        migrations.AddField(
            model_name='businesstripemployee',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 23, 15, 47, 9, 46933), verbose_name=b'Data ko\xc5\x84cowa'),
            preserve_default=False,
        ),
    ]
