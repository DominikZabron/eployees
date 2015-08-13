# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTrip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purpose', models.CharField(max_length=255, verbose_name=b'Cel wyjazdu')),
                ('begin_date', models.DateField(verbose_name=b'Rozpocz\xc4\x99cie')),
            ],
        ),
    ]
