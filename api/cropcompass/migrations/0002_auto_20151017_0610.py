# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cropcompass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawnassdata',
            name='state_ansi',
            field=models.CharField(max_length=24, null=True, blank=True),
        ),
    ]
