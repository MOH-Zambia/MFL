# from django.contrib import admin
from django.contrib.gis import admin
from .models import Province, District, Constituency, Ward, DistrictType, LocationType


# admin.site.register(WorldBorder, admin.GeoModelAdmin)

# admin.site.register(ZambiaBorder, admin.OSMGeoAdmin)

admin.site.register(Province, admin.OSMGeoAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'district_type')


class WardAdmin(admin.ModelAdmin):
    list_display = ('name', 'constituency', 'population')


admin.site.register(District, admin.OSMGeoAdmin)
admin.site.register(Constituency, admin.OSMGeoAdmin)
admin.site.register(Ward, admin.OSMGeoAdmin)
admin.site.register(DistrictType)
admin.site.register(LocationType)
