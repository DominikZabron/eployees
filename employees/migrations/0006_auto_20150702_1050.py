# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_auto_20150701_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'dodatkowe dane personalne', 'verbose_name_plural': 'dane osobowe'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(parent_link=True, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
