# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shutdown', '0002_auto_20160706_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shutdown',
            name='message',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
