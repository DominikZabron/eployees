# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0016_auto_20150825_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTripInvoiceAccomodation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('amount', models.DecimalField(verbose_name=b'Kwota', max_digits=9, decimal_places=2)),
                ('desc', models.TextField(verbose_name=b'Opis', blank=True)),
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
                ('amount', models.DecimalField(verbose_name=b'Kwota', max_digits=9, decimal_places=2)),
                ('desc', models.TextField(verbose_name=b'Opis', blank=True)),
                ('route', models.ForeignKey(verbose_name=b'Trasa', to='trips.BusinessTripRoute')),
                ('settlement', models.ForeignKey(verbose_name=b'Rozliczenie', to='trips.BusinessTripSettlement')),
            ],
            options={
                'verbose_name': 'Koszt podr\xf3\u017cy',
                'verbose_name_plural': 'Koszty podr\xf3\u017cy',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripInvoiceOther',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('amount', models.DecimalField(verbose_name=b'Kwota', max_digits=9, decimal_places=2)),
                ('desc', models.TextField(verbose_name=b'Opis', blank=True)),
                ('settlement', models.ForeignKey(verbose_name=b'Rozliczenie', to='trips.BusinessTripSettlement')),
            ],
            options={
                'verbose_name': 'Inny',
                'verbose_name_plural': 'Pozosta\u0142e koszty',
            },
        ),
        migrations.AlterField(
            model_name='businesstripallowance',
            name='is_first_day',
            field=models.BooleanField(default=True, verbose_name=b'Pierwszy dzie\xc5\x84 delegacji'),
        ),
        migrations.AddField(
            model_name='businesstripinvoiceaccomodation',
            name='overnight',
            field=models.ForeignKey(verbose_name=b'Nocleg', to='trips.BusinessTripAllowance'),
        ),
        migrations.AddField(
            model_name='businesstripinvoiceaccomodation',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Rozliczenie', to='trips.BusinessTripSettlement'),
        ),
    ]
