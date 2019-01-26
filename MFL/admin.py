from django.contrib import admin
from django.contrib.gis import admin
from MFL.models import *

admin.site.register(AdministrativeUnit)
admin.site.register(OperatingHours)
admin.site.register(OperationStatus)
admin.site.register(FacilityType)
admin.site.register(Ownership)
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(Infrastructure)
admin.site.register(Equipment)


class FacilityAdmin(admin.OSMGeoAdmin):
    fieldsets = [
        ('Signature Domain', {'fields': ['HMIS_Code', 'name', 'facility_type', 'operation_status',
                                         'administrative_unit', 'ownership', 'district', 'constituency', 'ward',
                                         'email', 'web_address', 'phone', 'mobile', 'fax', 'address_line1',
                                         'address_line2', 'postal_address', 'longitude', 'latitude', 'geom']}),
        ('Service Domain', {'fields': ['services', 'infrastructure', 'number_of_beds', 'number_of_cots',
                                       'number_of_nurses', 'number_of_doctors'], 'classes': ['collapse']}),
    ]

    list_display = ('id', 'HMIS_Code', 'name', 'district', 'province')
    list_filter = ['district']
    search_fields = ['name']


admin.site.register(Facility, FacilityAdmin)

