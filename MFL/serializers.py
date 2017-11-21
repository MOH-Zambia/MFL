from rest_framework import serializers
from MFL.models import Facility
from django.contrib.auth.models import User

class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facility
        fields = ('HMIS_Code', 'facility_name')