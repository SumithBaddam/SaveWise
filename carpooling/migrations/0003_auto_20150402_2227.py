# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0002_auto_20150401_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
