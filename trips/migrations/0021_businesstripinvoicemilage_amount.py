# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0020_remove_businesstripinvoicemilage_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstripinvoicemilage',
            name='amount',
            field=models.DecimalField(default=0, verbose_name=b'Kwota', max_digits=9, decimal_places=2),
            preserve_default=False,
        ),
    ]
