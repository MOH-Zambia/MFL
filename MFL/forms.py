from django import forms
from maps.models import Province, District, Constituency, Ward
from .models import Facility, FacilityType, Ownership, OperationStatus, Service, ServiceCategory


class SearchForm(forms.Form):
    # model = Facility
    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Facility Name',
            'id': 'name',
        }
    ))
    HMIS_Code = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'HMIS Code',
            'id': 'HMIS_Code',
        }
    ))
    service_category = forms.ModelChoiceField(required=False, queryset=ServiceCategory.objects.all(), empty_label="Select a service category...", widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'service_category',
        }
    ))
    service = forms.ModelChoiceField(required=False, queryset=Service.objects.all(), empty_label="Select a service...", widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'service',
        }
    ))
    facility_type = forms.ModelChoiceField(required=False, queryset=FacilityType.objects.all(), empty_label="Select a facility type...", widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'facility_type',
        }
    ))
    ownership = forms.ModelChoiceField(required=False, queryset=Ownership.objects.all(), empty_label="Select a facility owner...", widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'ownership',
        }
    ))
    operation_status = forms.ModelChoiceField(required=False, queryset=OperationStatus.objects.all(), empty_label="Select a operation status...", widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'operation_status',
        }
    ))
    province = forms.ModelChoiceField(required=False, queryset=Province.objects.all(), empty_label="Select a province...")
    district = forms.ModelChoiceField(required=False, queryset=District.objects.all(), empty_label="Select a district...")
    constituency = forms.ModelChoiceField(required=False, queryset=Constituency.objects.all(), empty_label="Select a constituency...")
    ward = forms.ModelChoiceField(required=False, queryset=Ward.objects.all(), empty_label="Select a ward...")
