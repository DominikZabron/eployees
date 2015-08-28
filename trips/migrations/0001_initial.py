# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTrip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purpose', models.CharField(max_length=255, verbose_name=b'Cel wyjazdu')),
                ('begin_date', models.DateField(verbose_name=b'Rozpocz\xc4\x99cie')),
                ('description', models.TextField(verbose_name=b'Opis', blank=True)),
            ],
            options={
                'verbose_name': 'Delegacja',
                'verbose_name_plural': 'Delegacje',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripAllowance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('begin_time', models.DateTimeField(verbose_name=b'Pocz\xc4\x85tek')),
                ('end_time', models.DateTimeField(verbose_name=b'Koniec')),
                ('is_first_day', models.BooleanField(default=True, verbose_name=b'Pierwszy dzie\xc5\x84 delegacji')),
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
            name='BusinessTripInvoiceAccomodation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('amount', models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2)),
                ('desc', models.TextField(verbose_name=b'Opis', blank=True)),
                ('overnight', models.ForeignKey(verbose_name=b'Nocleg', to='trips.BusinessTripAllowance')),
            ],
            options={
                'verbose_name': 'Koszt noclegu',
                'verbose_name_plural': 'Koszty noclegu',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripInvoiceFare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('amount', models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2)),
                ('desc', models.TextField(verbose_name=b'Opis', blank=True)),
            ],
            options={
                'verbose_name': 'Koszt podr\xf3\u017cy',
                'verbose_name_plural': 'Koszty podr\xf3\u017cy',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripInvoiceMilage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('amount', models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2)),
                ('desc', models.TextField(verbose_name=b'Opis', blank=True)),
                ('distance', models.DecimalField(verbose_name=b'Odleg\xc5\x82o\xc5\x9b\xc4\x87 [km]', max_digits=9, decimal_places=2)),
                ('car', models.ForeignKey(verbose_name=b'Pojazd', to='assets.Car')),
            ],
            options={
                'verbose_name': 'Rejestracja przebiegu pojazdu',
                'verbose_name_plural': 'Rejestracja przebiegu pojazd\xf3w',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripInvoiceOther',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('amount', models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2)),
                ('desc', models.TextField(verbose_name=b'Opis', blank=True)),
            ],
            options={
                'verbose_name': 'Inny',
                'verbose_name_plural': 'Pozosta\u0142e koszty',
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
                ('trip', models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripEmployee')),
            ],
            options={
                'verbose_name': 'Przejazd',
                'verbose_name_plural': 'Przejazdy',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripSettlement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'w', max_length=1, verbose_name=b'Decyzja', choices=[(b'w', b'Oczekuje'), (b'a', b'Rozliczono'), (b'r', b'Odrzucono')])),
                ('trip', models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripEmployee')),
            ],
            options={
                'verbose_name': 'Rozliczenie',
                'verbose_name_plural': 'Rozliczenia',
            },
        ),
        migrations.AddField(
            model_name='businesstripinvoiceother',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripSettlement'),
        ),
        migrations.AddField(
            model_name='businesstripinvoicemilage',
            name='route',
            field=models.ForeignKey(verbose_name=b'Trasa', to='trips.BusinessTripRoute'),
        ),
        migrations.AddField(
            model_name='businesstripinvoicemilage',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripSettlement'),
        ),
        migrations.AddField(
            model_name='businesstripinvoicefare',
            name='route',
            field=models.ForeignKey(verbose_name=b'Trasa', to='trips.BusinessTripRoute'),
        ),
        migrations.AddField(
            model_name='businesstripinvoicefare',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripSettlement'),
        ),
        migrations.AddField(
            model_name='businesstripinvoiceaccomodation',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripSettlement'),
        ),
        migrations.AddField(
            model_name='businesstripallowance',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Rozliczenie', to='trips.BusinessTripSettlement'),
        ),
    ]
