# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NassHarvestAcres',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('commodity', models.CharField(max_length=64, null=True, blank=True)),
                ('year', models.SmallIntegerField(null=True, blank=True)),
                ('region', models.CharField(max_length=32, null=True, blank=True)),
                ('harvested_acres', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
