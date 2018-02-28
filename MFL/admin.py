from django.contrib import admin
from MFL.models import *

admin.site.register(Province)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name','province')

admin.site.register(District, DistrictAdmin)

admin.site.register(AdministrativeUnit)
admin.site.register(OperatingHours)
admin.site.register(OperationalStatus)
admin.site.register(FacilityType)
admin.site.register(Ownership)
admin.site.register(Service)
admin.site.register(Infrastructure)
admin.site.register(Equipment)

class FacilityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Signature Domain', {'fields': ['HMIS_Code', 'facility_name', 'facility_type', 'operational_status', 'administrative_unit', 'ownership', 'district', 'longitude', 'latitude',
                                         'email', 'web_address', 'phone', 'mobile', 'fax', 'street_name', 'street_number', 'area_name', 'postal_address']}),
        ('Service Domain', {'fields': ['services', 'infrastructure', 'number_of_beds', 'number_of_cots', 'number_of_nurses','number_of_doctors'], 'classes': ['collapse']}),
    ]

    list_display = ('id', 'HMIS_Code', 'facility_name', 'district', 'province')
    list_filter = ['district']
    search_fields = ['facility_name']

admin.site.register(Facility, FacilityAdmin)

