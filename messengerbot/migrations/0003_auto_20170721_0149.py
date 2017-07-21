# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messengerbot', '0002_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='picture_1',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='picture_2',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='picture_state',
            field=models.IntegerField(default=1, max_length=250),
            preserve_default=True,
        ),
    ]
