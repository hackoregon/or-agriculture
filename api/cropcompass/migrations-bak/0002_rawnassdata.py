# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cropcompass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawNassData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_desc', models.CharField(default='', max_length=6, null=True, blank=True)),
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
                ('agg_level_desc', models.CharField(default='', max_length=71, blank=True)),
                ('state_ansi', models.IntegerField(default=0, null=True, blank=True)),
                ('state_fips_code', models.IntegerField(default=0, null=True, blank=True)),
                ('state_alpha', models.CharField(default='', max_length=2, blank=True)),
                ('state_name', models.CharField(default='', max_length=6, blank=True)),
                ('asd_code', models.IntegerField(default=0, null=True, blank=True)),
                ('asd_desc', models.CharField(default='', max_length=73, blank=True)),
                ('county_ansi', models.IntegerField(default=0, null=True, blank=True)),
                ('county_code', models.IntegerField(default=0, null=True, blank=True)),
                ('county_name', models.CharField(default='', max_length=10, blank=True)),
                ('region_desc', models.CharField(default='', max_length=10, blank=True)),
                ('zip_5', models.CharField(default='', max_length=10, blank=True)),
                ('watershed_code', models.CharField(default=False, max_length=255, null=True, blank=True)),
                ('watershed_desc', models.CharField(default='', max_length=10, blank=True)),
                ('congr_district_code', models.CharField(default='', max_length=10, blank=True)),
                ('country_code', models.IntegerField(default=0, null=True, blank=True)),
                ('country_name', models.CharField(max_length=255, null=True, blank=True)),
                ('location_desc', models.CharField(default='', max_length=116, blank=True)),
                ('year', models.IntegerField(default=0, null=True, blank=True)),
                ('freq_desc', models.CharField(default='', max_length=6, blank=True)),
                ('begin_code', models.IntegerField(default=0, null=True, blank=True)),
                ('end_code', models.IntegerField(default=0, null=True, blank=True)),
                ('reference_period_desc', models.CharField(default='', max_length=4, blank=True)),
                ('week_ending', models.DateTimeField(null=True, blank=True)),
                ('load_time', models.DateTimeField(null=True, blank=True)),
                ('value', models.CharField(max_length=32, null=True, blank=True)),
                ('cv_percent', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=5, blank=True)),
            ],
        ),
    ]
