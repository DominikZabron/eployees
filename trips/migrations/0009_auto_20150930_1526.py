# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_auto_20150929_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessTripInvoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nazwa')),
                ('amount', models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2)),
                ('desc', models.TextField(verbose_name=b'Opis', blank=True)),
                ('settlement', models.ForeignKey(verbose_name=b'Rozliczenie', to='trips.BusinessTripSettlement')),
            ],
            options={
                'verbose_name': 'Koszt',
                'verbose_name_plural': 'Koszty',
            },
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceaccomodation',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceaccomodation',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceaccomodation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceaccomodation',
            name='name',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceaccomodation',
            name='settlement',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicefare',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicefare',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicefare',
            name='id',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicefare',
            name='name',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicefare',
            name='settlement',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicemilage',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicemilage',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicemilage',
            name='id',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicemilage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoicemilage',
            name='settlement',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceother',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceother',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceother',
            name='id',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceother',
            name='name',
        ),
        migrations.RemoveField(
            model_name='businesstripinvoiceother',
            name='settlement',
        ),
        migrations.AlterField(
            model_name='businesstriproute',
            name='settlement',
            field=models.ForeignKey(verbose_name=b'Rozliczenie', to='trips.BusinessTripSettlement'),
        ),
        migrations.AddField(
            model_name='businesstripinvoiceaccomodation',
            name='businesstripinvoice_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='trips.BusinessTripInvoice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesstripinvoicefare',
            name='businesstripinvoice_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='trips.BusinessTripInvoice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesstripinvoicemilage',
            name='businesstripinvoice_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='trips.BusinessTripInvoice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesstripinvoiceother',
            name='businesstripinvoice_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='trips.BusinessTripInvoice'),
            preserve_default=False,
        ),
    ]
