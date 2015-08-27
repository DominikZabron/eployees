# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0018_auto_20150827_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstripinvoiceaccomodation',
            name='amount',
            field=models.DecimalField(default=100, verbose_name=b'Kwota', max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesstripinvoicefare',
            name='amount',
            field=models.DecimalField(default=100, verbose_name=b'Kwota', max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesstripinvoicemilage',
            name='amount',
            field=models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businesstripinvoiceother',
            name='amount',
            field=models.DecimalField(default=100, verbose_name=b'Kwota', max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
    ]
