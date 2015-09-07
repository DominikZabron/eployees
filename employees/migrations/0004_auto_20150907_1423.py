# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20150907_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.FileField(default=b'/avatars/pawn.jpg', upload_to=b'avatars'),
        ),
    ]
