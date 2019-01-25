from .models import *
from django.core.serializers import serialize
from django.http import HttpResponse


def feature_provinces(request):
    provinces = serialize('geojson', Province.objects.all())
    return HttpResponse(provinces, content_type='json')


def feature_districts(request):
    districts = serialize('geojson', District.objects.all())
    return HttpResponse(districts, content_type='json')


def feature_constituencies(request):
    constituencies = serialize('geojson', Constituency.objects.all())
    return HttpResponse(constituencies, content_type='json')


def feature_wards(request):
    wards = serialize('geojson', Ward.objects.all())
    return HttpResponse(wards, content_type='json')