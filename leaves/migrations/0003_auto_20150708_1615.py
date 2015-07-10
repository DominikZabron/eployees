# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0002_auto_20150708_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='approved_by',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='if_approved',
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(default='w', max_length=1, verbose_name=b'decyzja', choices=[(b'w', b'oczekuje'), (b'a', b'zaakceptowany'), (b'r', b'odrzucony')]),
            preserve_default=False,
        ),
    ]
