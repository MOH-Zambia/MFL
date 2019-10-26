from django.contrib import admin
from django.contrib.gis import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
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
        ('Signature Domain', {'fields': ['HMIS_code', 'smartcare_GUID', 'eLMIS_ID', 'iHRIS_ID', 'name', 'facility_type', 'operation_status',
                                         'administrative_unit', 'ownership', 'district', 'constituency', 'ward',
                                         'email', 'web_address', 'phone', 'mobile', 'fax', 'address_line1',
                                         'address_line2', 'postal_address', 'location_type', 'longitude', 'latitude', 'geom']}),
        ('Service Domain', {'fields': ['services', 'infrastructure', 'number_of_beds', 'number_of_cots',
                                       'number_of_nurses', 'number_of_doctors'], 'classes': ['collapse']}),
    ]

    list_display = ('id', 'HMIS_code', 'smartcare_GUID', 'eLMIS_ID', 'iHRIS_ID', 'name', 'facility_type', 'district', 'province')
    list_filter = ['district__province', 'district', 'facility_type', 'ownership']
    search_fields = ['name']


admin.site.register(Facility, FacilityAdmin)

