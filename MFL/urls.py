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
from django.conf.urls import include, url
from django.contrib import admin
from MFL.views import FacilityDetail, FacilityList, FacilityViewSet
from django.views.generic import TemplateView
from rest_framework import routers


app_name = 'MFL'

router = routers.DefaultRouter()
router.register(r'facility', FacilityViewSet)


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^facility/(?P<slug>\w+)/', FacilityDetail.as_view(), name='facility'),
    url(r'^search/', FacilityList.as_view(), name='search'),
    # url(r'^\?q=(?P<query>\w+)$', FacilityList.as_view(), name='search'),
    # url(r'^facility/all', FacilityList.as_view(), name='list'),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
