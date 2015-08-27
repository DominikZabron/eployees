# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0021_businesstripinvoicemilage_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstripinvoiceaccomodation',
            name='amount',
            field=models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='businesstripinvoicefare',
            name='amount',
            field=models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='businesstripinvoicemilage',
            name='amount',
            field=models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='businesstripinvoiceother',
            name='amount',
            field=models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2),
        ),
    ]
