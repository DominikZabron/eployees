# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstripemployee',
            name='employee',
            field=models.ForeignKey(related_name='emp', verbose_name=b'Pracownik', to=settings.AUTH_USER_MODEL),
        ),
    ]
