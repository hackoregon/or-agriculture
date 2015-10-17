from cropcompass import models
from rest_framework import serializers



class NassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RawNassData 


class NassBasicsSerializer(NassSerializer):
    class Meta:
        model = models.RawNassData 
        fields = (
            'year', 
            'commodity_desc', 
            'county_name', 
            'group_desc',
            'domain_desc',
            'class_desc',
            'short_desc',
            'statisticcat_desc',
            'unit_desc',
            #'freq_desc',
            'value',
            'value_raw',
        )

    value = serializers.SerializerMethodField('clean_value')
    value_raw = serializers.ReadOnlyField(source='value')


    def clean_value(self, obj):
        """ Remember 'value' is actually the name of a field. """
        num_string = obj.value.replace(',', '')
        try:
            if '.' in num_string:
                return float(num_string)
            else:
                return int(num_string)
        except ValueError:
                return None 


class NassCommodities(serializers.ModelSerializer):
    class Meta:
        model = models.RawNassData 

        fields = (
                'commodity_desc', 
                'group_desc',
                'sector_desc',
                'class_desc',
                )
