# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0002_auto_20150724_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTripItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trip_from', models.CharField(max_length=255, verbose_name=b'Miejsce pocz\xc4\x85tkowe')),
                ('begin_time', models.DateTimeField(verbose_name=b'Pocz\xc4\x85tek wyjazdu')),
                ('trip_to', models.CharField(max_length=255, verbose_name=b'Miejsce docelowe')),
                ('end_time', models.DateTimeField(verbose_name=b'Koniec wyjazdu')),
                ('transportation', models.CharField(max_length=1, verbose_name=b'\xc5\x9arodek transportu')),
                ('estimated_cost', models.DecimalField(verbose_name=b'Szacunkowy koszt', max_digits=9, decimal_places=2)),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wyjazd s\u0142u\u017cbowy',
                'verbose_name_plural': 'Wyjazdy s\u0142u\u017cbowe',
            },
        ),
        migrations.AlterModelOptions(
            name='businesstrip',
            options={'verbose_name': 'Delegacja', 'verbose_name_plural': 'Deleygacje'},
        ),
    ]
