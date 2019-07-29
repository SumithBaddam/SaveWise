# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seats', models.IntegerField()),
                ('status', models.BooleanField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('seats', models.IntegerField()),
                ('vehicle_number', models.CharField(max_length=10)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('user_details', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='request',
            name='vehicle',
            field=models.ForeignKey(default=0, to='carpooling.Vehicle'),
            preserve_default=True,
        ),
    ]
