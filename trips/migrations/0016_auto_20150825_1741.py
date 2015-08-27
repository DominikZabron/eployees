# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0015_auto_20150813_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTripAllowance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin_time', models.DateTimeField(verbose_name=b'Pocz\xc4\x85tek')),
                ('end_time', models.DateTimeField(verbose_name=b'Koniec')),
                ('is_first_day', models.BooleanField(verbose_name=b'Pierwszy dzie\xc5\x84 delegacji')),
                ('is_breakfast', models.BooleanField(verbose_name=b'\xc5\x9aniadanie')),
                ('is_dinner', models.BooleanField(verbose_name=b'Obiad')),
                ('is_supper', models.BooleanField(verbose_name=b'Kolacja')),
                ('is_commute_lump', models.BooleanField(verbose_name=b'Rycza\xc5\x82t za dojazdy')),
                ('is_accomodation_lump', models.BooleanField(verbose_name=b'Rycza\xc5\x82t za noclegi')),
            ],
            options={
                'verbose_name': 'Dieta',
                'verbose_name_plural': 'Diety',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripEmployee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estimated_cost', models.DecimalField(verbose_name=b'Szacunkowy koszt [z\xc5\x82]', max_digits=9, decimal_places=2)),
                ('status', models.CharField(default=b'w', max_length=1, verbose_name=b'Decyzja', choices=[(b'w', b'Oczekuje'), (b'a', b'Zaakceptowany'), (b'r', b'Odrzucony')])),
                ('business_trip', models.ForeignKey(verbose_name=b'Delegacja', to='trips.BusinessTrip')),
                ('employee', models.ForeignKey(verbose_name=b'Pracownik', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wyjazd s\u0142u\u017cbowy',
                'verbose_name_plural': 'Wyjazdy s\u0142u\u017cbowe',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripRoute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin', models.CharField(max_length=255, verbose_name=b'Miejsce pocz\xc4\x85tkowe')),
                ('begin_time', models.DateTimeField(verbose_name=b'Pocz\xc4\x85tek wyjazdu')),
                ('end', models.CharField(max_length=255, verbose_name=b'Miejsce docelowe')),
                ('end_time', models.DateTimeField(verbose_name=b'Koniec wyjazdu')),
                ('transportation', models.CharField(max_length=1, verbose_name=b'\xc5\x9arodek transportu', choices=[(b'c', b'samoch\xc3\xb3d firmowy'), (b'o', b'samoch\xc3\xb3d prywatny'), (b'r', b'pasa\xc5\xbcer'), (b'p', b'komunkacja publiczna'), (b't', b'poci\xc4\x85g'), (b'a', b'samolot')])),
                ('distance', models.IntegerField(verbose_name=b'Odleg\xc5\x82o\xc5\x9b\xc4\x87 [km]')),
                ('trip', models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripEmployee')),
            ],
            options={
                'verbose_name': 'Przejazd',
                'verbose_name_plural': 'Przejazdy',
            },
        ),
        migrations.RemoveField(
            model_name='businesstripitem',
            name='business_trip',
        ),
        migrations.RemoveField(
            model_name='businesstripitem',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='businesstripitem',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='businesstripsettlement',
            name='business_trip',
        ),
        migrations.RemoveField(
            model_name='businesstripsettlement',
            name='costs_all',
        ),
        migrations.RemoveField(
            model_name='businesstripsettlement',
            name='description',
        ),
        migrations.AlterField(
            model_name='businesstripsettlement',
            name='status',
            field=models.CharField(default=b'w', max_length=1, verbose_name=b'Decyzja', choices=[(b'w', b'Oczekuje'), (b'a', b'Rozliczono'), (b'r', b'Odrzucono')]),
        ),
        migrations.DeleteModel(
            name='BusinessTripItem',
        ),
        migrations.AddField(
            model_name='businesstripallowance',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Rozliczenie', to='trips.BusinessTripSettlement'),
        ),
        migrations.AddField(
            model_name='businesstripsettlement',
            name='trip',
            field=models.ForeignKey(default=1, verbose_name=b'Wyjazd', to='trips.BusinessTripEmployee'),
            preserve_default=False,
        ),
    ]
