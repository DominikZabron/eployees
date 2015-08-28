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
                ('user', models.OneToOneField(parent_link=True, related_name='leave', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Pracownik')),
                ('available_days', models.IntegerField(default=26, verbose_name=b'dni urlopu')),
            ],
            options={
                'verbose_name': 'urlop pracownika',
                'verbose_name_plural': 'urlopy pracownik\xf3w',
            },
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name=b'poczatek urlopu')),
                ('end_date', models.DateField(verbose_name=b'koniec urlopu')),
                ('days', models.IntegerField(verbose_name=b'dni urlopu')),
                ('status', models.CharField(default=b'w', max_length=1, verbose_name=b'decyzja', choices=[(b'w', b'Oczekuje'), (b'a', b'Zaakceptowany'), (b'r', b'Odrzucony')])),
                ('leave', models.ForeignKey(verbose_name=b'Pracownik', to='leaves.Leave')),
            ],
            options={
                'verbose_name': 'wniosek o urlop',
                'verbose_name_plural': 'wnioski urlopowe',
            },
        ),
    ]
