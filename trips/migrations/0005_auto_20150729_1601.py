# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20150729_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstripitem',
            name='transportation',
            field=models.CharField(max_length=1, verbose_name=b'\xc5\x9arodek transportu', choices=[(b'p', b'komunkacja publiczna'), (b'c', b'samoch\xc3\xb3d firmowy'), (b'o', b'samoch\xc3\xb3d prywatny'), (b'r', b'pasa\xc5\xbcer')]),
        ),
    ]
