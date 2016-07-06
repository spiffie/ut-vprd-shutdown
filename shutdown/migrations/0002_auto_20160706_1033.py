# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shutdown', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shutdown',
            name='path',
            field=models.CharField(help_text=b'Enter a full path, including leading slash, but NOT a trailing slash.', max_length=1000),
        ),
    ]
