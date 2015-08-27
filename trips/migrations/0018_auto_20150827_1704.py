# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20150707_1434'),
        ('trips', '0017_auto_20150826_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTripInvoiceMilage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('desc', models.TextField(verbose_name=b'Opis', blank=True)),
                ('distance', models.DecimalField(verbose_name=b'Odleg\xc5\x82o\xc5\x9b\xc4\x87 [km]', max_digits=9, decimal_places=2)),
                ('car', models.ForeignKey(verbose_name=b'Pojazd', to='assets.Car')),
            ],
            options={
                'verbose_name': 'Rejestracja przebiegu pojazdu',
                'verbose_name_plural': 'Rejestracja przebiegu pojazd\xf3w',
            },
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceaccomodation',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicefare',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceother',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='businesstriproute',
            name='distance',
        ),
        migrations.AlterField(
            model_name='businesstripinvoiceaccomodation',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripSettlement'),
        ),
        migrations.AlterField(
            model_name='businesstripinvoicefare',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Wyjazd', to='trips.BusinessTripSettlement'),
        ),
        migrations.AlterField(
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
    ]
