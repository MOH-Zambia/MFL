from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from MFL.models import Facility


class GeoFacilitySerializer(GeoFeatureModelSerializer):
    facility_type = serializers.StringRelatedField()
    ownership = serializers.StringRelatedField()
    operation_status = serializers.StringRelatedField()
    operating_hours = serializers.StringRelatedField(many=True)
    infrastructure = serializers.StringRelatedField(many=True)
    equipment = serializers.StringRelatedField(many=True)
    district = serializers.StringRelatedField()
    location_type = serializers.StringRelatedField()

    class Meta:
        model = Facility
        geo_field = 'geom'
        fields = ('id', 'DHIS2_UID', 'HMIS_Code', 'name', 'facility_type', 'operation_status', 'administrative_unit',
                  'ownership', 'services', 'lab_level', 'operating_hours', 'infrastructure', 'equipment',
                  'number_of_beds', 'number_of_cots', 'number_of_nurses', 'number_of_doctors', 'address_line1',
                  'address_line2', 'district', 'postal_address', 'location_type', 'web_address', 'email', 'phone',
                  'mobile', 'fax', 'catchment_population', 'longitude', 'latitude', 'geom', 'updated', 'timestamp')


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    facility_type = serializers.StringRelatedField()
    ownership = serializers.StringRelatedField()
    operation_status = serializers.StringRelatedField()
    operating_hours = serializers.StringRelatedField(many=True)
    infrastructure = serializers.StringRelatedField(many=True)
    equipment = serializers.StringRelatedField(many=True)
    district = serializers.StringRelatedField()
    location_type = serializers.StringRelatedField()

    class Meta:
        model = Facility
        geo_field = 'geom'
        fields = ('id', 'DHIS2_UID', 'HMIS_Code', 'name', 'facility_type', 'operation_status', 'administrative_unit',
                  'ownership', 'services', 'lab_level', 'operating_hours', 'infrastructure', 'equipment',
                  'number_of_beds', 'number_of_cots', 'number_of_nurses', 'number_of_doctors', 'address_line1',
                  'address_line2', 'district', 'postal_address', 'location_type', 'web_address', 'email', 'phone',
                  'mobile', 'fax', 'catchment_population', 'longitude', 'latitude', 'geom', 'updated', 'timestamp')
