# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='year',
            field=models.IntegerField(default=2015, verbose_name=b'dotyczy roku kalendarzowego'),
            preserve_default=False,
        ),
    ]
