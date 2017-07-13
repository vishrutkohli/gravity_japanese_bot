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
            name='modeOfContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modeOfContact', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('signatureOnDelivery', models.CharField(default=b'NULL', max_length=250)),
                ('description', models.CharField(default=b'NULL', max_length=250)),
                ('orderID', models.CharField(default=b'NULL', max_length=250)),
                ('addressFrom', models.ForeignKey(related_name=b'addressFrom', to='messengerbot.address')),
                ('addressTo', models.ForeignKey(related_name=b'addressTo', to='messengerbot.address')),
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
            name='statusCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='typeOfBox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeOfBox', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='typeOfCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeOfCollection', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='typeOfService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeOfService', models.CharField(default=b'NULL', max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='typeOfShipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeOfShipment', models.CharField(default=b'NULL', max_length=250)),
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
            field=models.ForeignKey(related_name=b'statusMessage', to='messengerbot.statusCode'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='fbid',
            field=models.ForeignKey(to='messengerbot.user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='modeOfContact',
            field=models.ForeignKey(to='messengerbot.modeOfContact'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(to='messengerbot.status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='typeOfBox',
            field=models.ForeignKey(to='messengerbot.typeOfBox'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='typeOfCollection',
            field=models.ForeignKey(to='messengerbot.typeOfCollection'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='typeOfService',
            field=models.ForeignKey(to='messengerbot.typeOfService'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='typeOfShipment',
            field=models.ForeignKey(to='messengerbot.typeOfShipment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='fbid',
            field=models.ManyToManyField(to='messengerbot.user', null=True),
            preserve_default=True,
        ),
    ]
