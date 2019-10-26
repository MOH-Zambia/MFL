# from django.contrib import admin
from django.contrib.gis import admin
from .models import Province, District, Constituency, Ward, DistrictType, LocationType

admin.site.register(Province, admin.OSMGeoAdmin)


class DistrictAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'province', 'district_type')


class ConstituencyAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'district', 'population')
    list_filter = ['district']
    search_fields = ['name']


class WardAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'constituency', 'population')
    list_filter = ['constituency']
    search_fields = ['name']


admin.site.register(District, admin.OSMGeoAdmin)
admin.site.register(Constituency, ConstituencyAdmin)
admin.site.register(Ward, WardAdmin)
admin.site.register(DistrictType)
admin.site.register(LocationType)
