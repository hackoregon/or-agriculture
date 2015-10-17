# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cropcompass', '0002_rawnassdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawnassdata',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 5, 4, 42, 470885, tzinfo=utc), verbose_name='Date Created', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rawnassdata',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 5, 4, 48, 987284, tzinfo=utc), verbose_name='Last Modified', auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='agg_level_desc',
            field=models.CharField(max_length=71, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='asd_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='asd_desc',
            field=models.CharField(max_length=73, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='begin_code',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='congr_district_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='country_code',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='county_ansi',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='county_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='county_name',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='cv_percent',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='end_code',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='freq_desc',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='load_time',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='location_desc',
            field=models.CharField(max_length=116, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='reference_period_desc',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='region_desc',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='source_desc',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='state_alpha',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='state_ansi',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='state_fips_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='state_name',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='watershed_code',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='watershed_desc',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='week_ending',
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='year',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rawnassdata',
            name='zip_5',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
