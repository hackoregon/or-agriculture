from django.conf.urls import url, include
from rest_framework import routers
from cropcompass import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'crop_sales_by_year', views.NassSalesByYear, 
        base_name='sales_by_year')
router.register(r'crops_list', views.NassCrops, 
        base_name='crops')
router.register(r'counties_list', views.NassCounties, 
        base_name='counties')
router.register(r'crop_production', views.NassProduction, 
        base_name='production')
router.register(r'crop_sales', views.NassSales, 
        base_name='sales')
router.register(r'nass_basics', views.NassBasicsViewSet, 
        base_name='basics')
router.register(r'nass_commodities', views.NassCommodities, 
        base_name='commodities')
router.register(r'nass_raw', views.NassViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
