# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpooling', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='user_details',
            new_name='user',
        ),
    ]
