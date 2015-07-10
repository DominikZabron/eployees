# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0003_auto_20150708_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leave',
            options={'verbose_name': 'urlop pracownika', 'verbose_name_plural': 'urlopy pracownik\xf3w'},
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(max_length=1, verbose_name=b'decyzja', choices=[(b'w', b'Oczekuje'), (b'a', b'Zaakceptowany'), (b'r', b'Odrzucony')]),
        ),
    ]
