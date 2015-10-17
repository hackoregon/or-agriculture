from cropcompass import models
from cropcompass import filters
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

    value = serializers.SerializerMethodField('normalize_value')
    value_raw = serializers.ReadOnlyField(source='value')

    def normalize_value(self, obj):
        # this could happen in the model instead, but
        # this is a good place for other clean up functions.
        return filters.normalize_value_field(obj.value)



class NassCommodities(serializers.ModelSerializer):
    class Meta:
        model = models.RawNassData 

        fields = (
                'commodity_desc', 
                'group_desc',
                'sector_desc',
                'class_desc',
                )
