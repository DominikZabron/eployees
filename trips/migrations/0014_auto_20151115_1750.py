# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0013_auto_20151115_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstripinvoiceaccomodation',
            name='scan',
            field=models.ImageField(default=1, upload_to=b'content/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesstripinvoiceother',
            name='scan',
            field=models.ImageField(default=1, upload_to=b'content/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
