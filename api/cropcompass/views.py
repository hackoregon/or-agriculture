from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from cropcompass import models
from cropcompass.models import RawNassData as NASS
from cropcompass import serializers
from cropcompass import filters
import pandas as pd




class NassBasicsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NassBasicsSerializer

    queryset = NASS.objects.filter(
       freq_desc='ANNUAL',
       year__isnull=False,
       commodity_desc__isnull=False,
       county_name__isnull=False,
    )

    paginate_by = 100

    filter_fields = (
            'year', 
            'commodity_desc', 
            'county_name', 
            'group_desc',
            'domain_desc',
            'class_desc',
            'freq_desc',
            'unit_desc',
            'statisticcat_desc',
            )

    search_fields = ('$short_desc',)
    ordering_fields = ('__all__')



class NassCommodities(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NassCommodities

    queryset = NASS.objects.filter(
            sector_desc__in=[
                'HORTICULTURE',
                'ANIMALS & PRODUCTS',
                'CROPS',]
            ).distinct(

                'commodity_desc', 
                'group_desc',
                'sector_desc',
                'class_desc',
                )

    paginate_by = 1000



class NassCounties(viewsets.ViewSet):

    def list(self, request):
        counties = NASS.objects.values_list(
                'county_name', flat=True).filter(
                county_name__isnull=False
                ).order_by('county_name').distinct()
        counties = map(unicode.title, counties)
        return Response(counties)



class NassCrops(viewsets.ViewSet):

    def list(self, request):
        crops = NASS.objects.values_list(
                'commodity_desc', flat=True).filter(
                commodity_desc__isnull=False,
                sector_desc__in=[
                    'HORTICULTURE',
                    'ANIMALS & PRODUCTS',
                    'CROPS',]
                ).order_by('commodity_desc').distinct()
        crops = map(unicode.title, crops)
        return Response(crops)



class NassSalesByYear(viewsets.ViewSet):
    """
    Mainly a test view for using Pandas to pivot and aggregate data.
    """
    
    def list(self, request):
        crops = NASS.objects.filter(
                #statisticcat_desc__icontains='SALES',
                unit_desc='$',
                sector_desc__in=[
                    'HORTICULTURE',
                    'ANIMALS & PRODUCTS',
                    'CROPS',],
                #freq_desc='ANNUAL',
                #year__isnull=False,
                #commodity_desc__isnull=False,
                #county_name__isnull=False,
                )
        
        df = pd.DataFrame.from_records(crops.values())
        df.value = df.value.apply(filters.normalize_value_field)
        pt = df.pivot_table(
                index='year', 
                columns='commodity_desc',
                values='value', 
                aggfunc=sum).sort_index(1)

        return Response(pt.to_dict())



class NassProduction(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NassBasicsSerializer

    queryset = NASS.objects.filter(
            statisticcat_desc='AREA IN PRODUCTION',
            sector_desc__in=[
                'HORTICULTURE',
                'ANIMALS & PRODUCTS',
                'CROPS',],
            freq_desc='ANNUAL',
            year__isnull=False,
            commodity_desc__isnull=False,
            county_name__isnull=False,)

    paginate_by = 200
    ordering = ('commodity_desc', 'year', 'county_name')

    filter_fields = (
            'year', 
            'commodity_desc', 
            'county_name', 
            'group_desc',
            'domain_desc',
            'class_desc',
            'unit_desc',
            'statisticcat_desc',
            )

    search_fields = ('=county_name', '=year', '$short_desc',)
    ordering_fields = ('__all__')



class NassSales(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NassBasicsSerializer

    queryset = NASS.objects.filter(
            statisticcat_desc='SALES',
            unit_desc='$',
            sector_desc__in=[
                'HORTICULTURE',
                'ANIMALS & PRODUCTS',
                'CROPS',],
            freq_desc='ANNUAL',
            year__isnull=False,
            commodity_desc__isnull=False,
            county_name__isnull=False,)

    paginate_by = 200
    ordering = ('commodity_desc', 'year', 'county_name')

    filter_fields = (
            'year', 
            'commodity_desc', 
            'county_name', 
            'group_desc',
            'domain_desc',
            'class_desc',
            'unit_desc',
            'statisticcat_desc',
            )

    search_fields = ('=county_name', '=year', '$short_desc',)
    ordering_fields = ('__all__')



class NassAllCommodities(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NassCommodities

    queryset = NASS.objects.all().distinct(
                'commodity_desc', 
                'group_desc',
                'sector_desc',
                'class_desc',
                )

    paginate_by = 2000



class NassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NASS.objects.all()
    serializer_class = serializers.NassSerializer
    #ordering = ('year', 'region', 'commodity')
    filter_fields = (
            'year', 
            'commodity_desc', 
            'county_name', 
            'group_desc',
            'domain_desc',
            'class_desc',
            'freq_desc',
            'statisticcat_desc',
            'unit_desc',
            )
    search_fields = ('$short_desc',)
    ordering_fields = ('__all__')
