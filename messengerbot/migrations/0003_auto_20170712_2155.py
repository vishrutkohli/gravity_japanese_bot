# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messengerbot', '0002_auto_20170712_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='timestamp',
            field=models.DateTimeField(default=b'NULL', max_length=250),
        ),
    ]
