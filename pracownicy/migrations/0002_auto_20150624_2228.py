# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pracownicy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pracownik',
            old_name='first_name',
            new_name='fname_text',
        ),
        migrations.RenameField(
            model_name='pracownik',
            old_name='second_name',
            new_name='lname_text',
        ),
    ]
