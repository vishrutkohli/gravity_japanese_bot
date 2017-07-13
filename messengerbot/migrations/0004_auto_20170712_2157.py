# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messengerbot', '0003_auto_20170712_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
