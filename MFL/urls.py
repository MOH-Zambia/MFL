"""MFL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.gis import admin
from django.urls import include, path
from django.conf.urls import url
from MFL.views import FacilityDetail, FacilityList, FacilityTable, FacilityViewSet, FeatureFacilityViewSet, feature_facilities, MapView
from django.views.generic import TemplateView
from rest_framework import routers

app_name = 'MFL'

facility_list = FacilityViewSet.as_view({
    'get': 'list'
})
facility_detail = FacilityViewSet.as_view({
    'get': 'retrieve'
})

router = routers.DefaultRouter()
router.register(r'facility', FacilityViewSet)
router.register(r'feature/facility', FeatureFacilityViewSet)

# router = routers.DefaultRouter()
# router.register(r'facility', FacilityViewSet)


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    # url(r'^facility/(?P<pk>\d+)$', FacilityDetail.as_view(), name='facility'),
    path('facility/<int:pk>', FacilityDetail.as_view(), name='facility'),
    path('map', MapView.as_view(), name='map'),
    path('features/facility', feature_facilities, name='facilities'),
    path('list', FacilityList.as_view(), name='list'),
    path('table', FacilityTable.as_view(), name='table'),
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('api/', include(router.urls)),
    path('admin', admin.site.urls),
    path('', include('geography.urls')),
]
