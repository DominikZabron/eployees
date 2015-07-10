# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('user', models.OneToOneField(parent_link=True, related_name='leave', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('available_days', models.IntegerField(default=26)),
            ],
            options={
                'verbose_name': 'urlop pracownika',
                'verbose_name_plural': 'urlopy pracownikow',
            },
        ),
    ]
