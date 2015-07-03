# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20150703_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_company_owned',
            field=models.BooleanField(verbose_name=b'Wlasnosc firmy'),
        ),
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
