# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0004_auto_20150710_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='user',
            field=models.OneToOneField(parent_link=True, related_name='leave', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Pracownik'),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(default=b'w', max_length=1, verbose_name=b'decyzja', choices=[(b'w', b'Oczekuje'), (b'a', b'Zaakceptowany'), (b'r', b'Odrzucony')]),
        ),
    ]
