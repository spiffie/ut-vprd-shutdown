# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shutdown',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=1000)),
                ('message', models.CharField(max_length=1000)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('is_exact_match', models.BooleanField(default=False, help_text=b'Select to shutdown only exact path matches.')),
            ],
            options={
                'ordering': ('-start_time', 'path'),
                'db_table': 'REGR_SHUTDOWN',
                'managed': True,
            },
        ),
    ]
