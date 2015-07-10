# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leaves', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name=b'poczatek urlopu')),
                ('end_date', models.DateField(verbose_name=b'koniec urlopu')),
                ('days', models.IntegerField(verbose_name=b'dni urlopu')),
                ('if_approved', models.NullBooleanField(verbose_name=b'decyzja')),
                ('approved_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'wniosek o urlop',
                'verbose_name_plural': 'wnioski urlopowe',
            },
        ),
        migrations.AlterField(
            model_name='leave',
            name='available_days',
            field=models.IntegerField(default=26, verbose_name=b'dni urlopu'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='leave',
            field=models.ForeignKey(to='leaves.Leave'),
        ),
    ]
