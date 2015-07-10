# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20150703_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'pojazd', 'verbose_name_plural': 'pojazdy'},
        ),
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(verbose_name=b'Pracownik', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
