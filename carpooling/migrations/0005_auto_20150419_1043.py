# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carpooling', '0004_auto_20150417_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='find_request',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='find_request',
            name='user_requesting',
            field=models.ForeignKey(related_name='find_request_requesting', default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='find_request',
            name='user',
            field=models.ForeignKey(related_name='find_request_requested', default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 10, 43, 4, 553032), blank=True),
            preserve_default=True,
        ),
    ]
