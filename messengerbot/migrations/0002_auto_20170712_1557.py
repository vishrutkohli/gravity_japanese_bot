# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messengerbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='country',
            field=models.ForeignKey(to='messengerbot.country'),
        ),
    ]
