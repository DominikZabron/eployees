# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20150915_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.FileField(default=b'/media/avatars/pawn.jpg', upload_to=b'avatars'),
        ),
        migrations.AlterField(
            model_name='qualificationsemployee',
            name='qualifications',
            field=models.ForeignKey(verbose_name=b'uprawnienia', to='employees.Qualifications', unique=True),
        ),
    ]
