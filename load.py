import os
import csv
from django.contrib.gis.utils import LayerMapping
from MFL.models import *
from maps.models import *


provinces_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'maps/data', 'Province.shp'),
)

districts_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'maps/data', 'District.shp'),
)

constituencies_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'maps/data', 'Constituent.shp'),
)

wards_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'maps/data', 'Ward.shp'),
)

facility_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'maps/data', 'Facility.shp'),
)

# Auto-generated `LayerMapping` dictionary for ZambiaProvince model
province_mapping = {
    'name': 'NAME',
    'population': 'POPULATION',
    'pop_density': 'POP_DENSIT',
    'area_sq_km': 'AREA_SQ_KM',
    'geom': 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for ZambiaDistrict model
district_mapping = {
    'name': 'NAME',
    'district_type': {'name': 'FEATURE_TY'},
    'province': {'name': 'PROVINCE'},
    'population': 'POPULATION',
    'pop_density': 'POP_DENSIT',
    'area_sq_km': 'AREA_SQ_KM',
    'geom': 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for ZambiaConstituency model
constituency_mapping = {
    'name': 'NAME',
    'district': {'name': 'DISTRICT'},
    'population': 'POPULATION',
    'pop_density': 'POP_DENSIT',
    'area_sq_km': 'AREA_SQ_KM',
    'geom': 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for ZambiaWard model
ward_mapping = {
    'name': 'NAME',
    'population': 'POPULATION',
    'pop_density': 'POP_DENSIT',
    'area_sq_km': 'AREA_SQ_KM',
    'geom': 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for ZambiaWard model
facility_mapping = {
    'district': {'name': 'DISTRICT'},
    'name': 'NAME',
    'HMIS_Code': 'HMIS_CODE',
    'location_type': {'name': 'LOCATION'},
    'ownership': {'name': 'OWNERSHIP'},
    'facility_type': {'name': 'FACILITY_T'},
    # 'operational_status': {'name': 'OPERATIONA'},
    'catchment_population': 'CATCHMENT_',
    'longitude': 'LONGITUDE',
    'latitude': 'LATITUDE',
    'geom': 'POINT',
}


def load_operational_status_table():
    data = {
        'Operational': 'A facility that is open and serving patients',
        'Licensed': 'A facility that has been approved and issued a license by the appropriate national regulatory '
                    'body, but facility is not yet operational.',
        'Pending Licensing': 'A facility that has been recommended by the district health management team, '
                             'but is waiting for a license from the national regulatory body.',
        'License Suspended': 'A facility whose license has been temporarily stopped for reasons including '
                             'selfrequest, sickness, disciplinary action, etc.',
        'License Cancelled': 'A facility whose license has been permanently stopped by the national body.',
        'Pending Registration': 'A facility that has been approved by the local authorities as an institution and a '
                                'request for official registration have been submitted and with approval pending.',
        'Registered': 'A facility that has been approved as an institution and a registration number given.',
        'Closed': 'A facility that has a valid license, but which has permanently closed.',
        'Invalid': 'A facility where the attributes of a facility (name, location, etc.) are different than those on '
                   'the facility’s license.',
        'Does not exist': 'A facility which has been licensed, but has been verified not to physically exist.',
        'Duplicate': 'The facility exists and is properly licensed, but is an effective duplicate of another '
                     'facility. This usually occurs when two data sources are merged together, with slightly '
                     'different names but refer to the same facility. '
    }

    for status, desc in data.items():
        OperationStatus.objects.create(name=status, description=desc)
        print('Saved: OperationalStatus => ' + status)

    print('Completed loading OperationalStatus table!')


def load_ownership_table():
    data = ['GRZ', 'Private', 'Faith Based', 'Military', 'NGO']

    for ownership in data:
        Ownership.objects.create(name=ownership)
        print('Saved: Ownership => '+ownership)

    print('Completed loading ownership table!')


def load_facility_type_table():
    data = [
        'Health Post',
        'Rural Health Centre',
        'Urban Health Centre',
        'Level 1 Hospital District',
        'Level 2 Hospital Provincial',
        'Level 3 Hospital Tertiary',
        'Military',
        'Private',
    ]

    for facility_type in data:
        FacilityType.objects.create(name=facility_type)
        print('Saved: FacilityType => ' + facility_type)

    print('Completed loading FacilityType table!')


def load_service_category_table():
    data = ['Accident and Emergency Casualty Service',
            'Ambulatory Services',
            'Antenatal Care',
            'Blood Transfusion Services',
            'Curative Services',
            ]

    for service_category in data:
        ServiceCategory.objects.create(name=service_category)
        print('Saved: ServiceCategory => '+service_category)

    print('Completed loading ServiceCategory table!')


def load_district_type_table():
    data = ['City', 'Provincial Town', 'District Town']
    for district_type in data:
        DistrictType.objects.create(name=district_type)
        print('Saved: DistrictType => ' + district_type)

    print('Completed loading DistrictType table!')


def load_location_type_table():
    data = ['Urban', 'Peri-Urban', 'Rural']
    for location_type in data:
        LocationType.objects.create(name=location_type)
        print('Saved: LocationType => ' + location_type)

    print('Completed loading LocationType table!')


def load_operating_hours_table():
    data = ['Open whole day', 'Open 24hrs', 'Open weekends', 'Open public holidays']
    for operating_hour_type in data:
        OperatingHours.objects.create(name=operating_hour_type)
        print('Saved: OperatingHours => ' + operating_hour_type)

    print('Completed loading OperatingHours table!')


# def transform_district_table():
#     District.objects.all().update(name=_name.upper())


# def load_provinces(apps, schema_editor):
#     with open('maps/data/data.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         # csv_reader = csv.DictReader(csvfile)
#
#         line_count = 0
#         output_rows = []
#
#         next(csv_reader)
#
#         for row in csv_reader:
#             # province = Province(name=row['name'], population=row['population'], pop_density=row['pop_density'],
#             # area_sq_km=row['area_sq_km']) province.save()
#             Province.objects.create(name=row[0], population=row[1], pop_density=row[2], area_sq_km=row[3], geom=row[4])


def update_wards_table():
    qs = Ward.objects.all()

    for ward in qs:
        constituent = Constituency.objects.filter(geom__contains=ward.geom)
        if constituent:
            ward.constituency = constituent[0]
            ward.save()
            print('Saved ward ' + ward.name + ' => ' + constituent[0].name)


def update_facilities_table():
    qs = Facility.objects.all()

    for facility in qs:
        constituent = Constituency.objects.filter(geom__contains=facility.geom)
        ward = Ward.objects.filter(geom__contains=facility.geom)

        if constituent:
            facility.constituency = constituent[0]
            facility.save()
            print('Saved facility ' + facility.name + ': Constituent => ' + constituent[0].name)

        if ward:
            facility.ward = ward[0]
            facility.save()
            print('Saved facility ' + facility.name + ': Ward => ' + ward[0].name)


def run(verbose=True):
    load_facility_type_table()
    load_operational_status_table()
    load_ownership_table()

    lm = LayerMapping(Province, provinces_shp, province_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

    load_district_type_table()
    load_location_type_table()

    lm = LayerMapping(District, districts_shp, district_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

    lm = LayerMapping(Constituency, constituencies_shp, constituency_mapping, transform=False)
    lm.save(strict=False, verbose=verbose)

    lm = LayerMapping(Ward, wards_shp, ward_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

    lm = LayerMapping(Facility, facility_shp, facility_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

    update_wards_table()

    update_facilities_table()
