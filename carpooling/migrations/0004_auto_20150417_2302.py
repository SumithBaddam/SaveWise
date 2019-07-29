# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carpooling', '0003_auto_20150402_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='find_request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latLocation', models.FloatField(default=0)),
                ('lonLocation', models.FloatField(default=0)),
                ('user', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 23, 2, 8, 234330), blank=True),
            preserve_default=True,
        ),
    ]
