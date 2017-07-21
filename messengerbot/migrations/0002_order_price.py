# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messengerbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.CharField(default=b'NULL', max_length=250),
            preserve_default=True,
        ),
    ]
