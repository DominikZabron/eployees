# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0012_auto_20151115_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstripinvoicefare',
            name='scan',
            field=models.ImageField(upload_to=b'content/%Y/%m/%d'),
        ),
    ]
