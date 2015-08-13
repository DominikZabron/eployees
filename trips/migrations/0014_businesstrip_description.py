# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0013_auto_20150813_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstrip',
            name='description',
            field=models.TextField(verbose_name=b'Opis', blank=True),
        ),
    ]
