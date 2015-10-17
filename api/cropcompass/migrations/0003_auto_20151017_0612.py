# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cropcompass', '0002_auto_20151017_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawnassdata',
            name='agg_level_desc',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='asd_code',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='asd_desc',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='congr_district_code',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='county_ansi',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='county_code',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='county_name',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='cv_percent',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='location_desc',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='region_desc',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='state_alpha',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='state_fips_code',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='state_name',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='watershed_desc',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='zip_5',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]
