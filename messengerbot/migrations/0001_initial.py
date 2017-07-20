# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'NULL', max_length=250)),
                ('address', models.CharField(default=b'NULL', max_length=250)),
                ('zipCode', models.CharField(default=b'NULL', max_length=250)),
                ('email', models.CharField(default=b'NULL', max_length=250)),
                ('phone', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='mode_of_contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mode_of_contact', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(default=b'NULL', max_length=250)),
                ('signature_on_delivery', models.CharField(default=b'NULL', max_length=250)),
                ('description', models.CharField(default=b'NULL', max_length=250)),
                ('order_id', models.CharField(default=b'NULL', max_length=250)),
                ('fbid', models.CharField(default=b'NULL', max_length=250)),
                ('type_of_service', models.CharField(default=b'NULL', max_length=250)),
                ('status', models.CharField(default=b'NULL', max_length=250)),
                ('address_from', models.CharField(default=b'NULL', max_length=250)),
                ('address_to', models.CharField(default=b'NULL', max_length=250)),
                ('type_of_shipment', models.CharField(default=b'NULL', max_length=250)),
                ('mode_of_contact', models.CharField(default=b'NULL', max_length=250)),
                ('type_of_collection', models.CharField(default=b'NULL', max_length=250)),
                ('type_of_box', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'NULL', max_length=250)),
                ('timezone', models.CharField(default=b'NULL', max_length=250)),
                ('country', models.ForeignKey(to='messengerbot.country')),
                ('languages', models.ManyToManyField(to='messengerbot.language', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(null=True, blank=True)),
                ('location', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='status_code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='type_of_box',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_box', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='type_of_collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_collection', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='type_of_service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_service', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='type_of_shipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_shipment', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(default=b'NULL', max_length=250)),
                ('fbid', models.CharField(default=b'NULL', max_length=250)),
                ('name', models.CharField(default=b'NULL', max_length=250)),
                ('email', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='status',
            name='status',
            field=models.ForeignKey(related_name=b'statusMessage', to='messengerbot.status_code'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='fbid',
            field=models.ManyToManyField(to='messengerbot.user', null=True),
            preserve_default=True,
        ),
    ]
