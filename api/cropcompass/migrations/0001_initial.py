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
        migrations.CreateModel(
            name='RawNassData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('source_desc', models.CharField(max_length=32, null=True, blank=True)),
                ('sector_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('group_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('commodity_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('class_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('prodn_practice_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('util_practice_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('statisticcat_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('unit_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('short_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('domain_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('domaincat_desc', models.CharField(max_length=255, null=True, blank=True)),
                ('agg_level_desc', models.CharField(max_length=71, null=True, blank=True)),
                ('state_ansi', models.CharField(max_length=10, null=True, blank=True)),
                ('state_fips_code', models.CharField(max_length=10, null=True, blank=True)),
                ('state_alpha', models.CharField(max_length=2, null=True, blank=True)),
                ('state_name', models.CharField(max_length=24, null=True, blank=True)),
                ('asd_code', models.CharField(max_length=10, null=True, blank=True)),
                ('asd_desc', models.CharField(max_length=73, null=True, blank=True)),
                ('county_ansi', models.CharField(max_length=10, null=True, blank=True)),
                ('county_code', models.CharField(max_length=10, null=True, blank=True)),
                ('county_name', models.CharField(max_length=10, null=True, blank=True)),
                ('region_desc', models.CharField(max_length=10, null=True, blank=True)),
                ('zip_5', models.CharField(max_length=10, null=True, blank=True)),
                ('watershed_code', models.CharField(max_length=255, null=True, blank=True)),
                ('watershed_desc', models.CharField(max_length=10, null=True, blank=True)),
                ('congr_district_code', models.CharField(max_length=10, null=True, blank=True)),
                ('country_code', models.CharField(max_length=32, null=True, blank=True)),
                ('country_name', models.CharField(max_length=255, null=True, blank=True)),
                ('location_desc', models.CharField(max_length=116, null=True, blank=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('freq_desc', models.CharField(max_length=32, null=True, blank=True)),
                ('begin_code', models.CharField(max_length=32, null=True, blank=True)),
                ('end_code', models.CharField(max_length=32, null=True, blank=True)),
                ('reference_period_desc', models.CharField(max_length=32, null=True, blank=True)),
                ('week_ending', models.CharField(max_length=32, null=True, blank=True)),
                ('load_time', models.CharField(max_length=32, null=True, blank=True)),
                ('value', models.CharField(max_length=32, null=True, blank=True)),
                ('cv_percent', models.CharField(max_length=12, null=True, blank=True)),
            ],
        ),
    ]
