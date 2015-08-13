# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_auto_20150729_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstripitem',
            name='status',
            field=models.CharField(default='w', max_length=1, verbose_name=b'Decyzja', choices=[(b'w', b'Oczekuje'), (b'a', b'Zaakceptowany'), (b'r', b'Odrzucony')]),
            preserve_default=False,
        ),
    ]
