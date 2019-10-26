__author__ = 'Chisanga L. Siwale <chisanga.siwale@moh.gov.zm>'

import csv
import logging
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
from django_seed import Seed

from MFL.models import Facility, FacilityType, OperationStatus, Ownership
from geography.models import Province, District, LocationType

seeder = Seed.seeder()
DATA_FILENAME = 'geography/data/data.csv'
csvfile = Path(__file__).parents[3] / DATA_FILENAME

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run(self, options['mode'])
        self.stdout.write('done.')


def load_facilities():
    """Creates a facility object from csv file"""
    logging.info("Loading facilities...")
    with open(csvfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_count = 0
        output_rows = []

        next(csv_reader)

        for row in csv_reader:
            Facility(
                district=District.objects.get(name=row[1]),
                name=row[2],
                HMIS_code=row[3],
                DHIS2_UID=row[4],
                smartcare_GUID=row[5],
                eLMIS_ID=row[6],
                iHRIS_ID=row[7],
                location_type=LocationType.objects.get(name=row[8]),
                ownership=Ownership.objects.get(name=row[9]),
                facility_type=FacilityType.objects.get(name=row[10]),
                # catchment_population_head_count=int(row[13]),
                # catchment_population_cso=int(row[14]),
                operation_status=OperationStatus.objects.get(name=row[15])
            ).save()

    #     for row in csv_reader:
    #         seeder.add_entity(Facility, {
    #             'province': row[0],
    #             'district': row[1],
    #             'name': row[2],
    #             'HMIS_code': row[3],
    #             'DHIS2_UID': row[4],
    #             'smartcare_GUID': row[5],
    #             'eLMIS_ID': row[6],
    #             'iHRIS_ID': row[7],
    #             'location': row[8],
    #             'ownership': row[9],
    #             'facility_type': row[10],
    #             'longitude': row[11],
    #             'latitude': row[12],
    #             'catchment_population_head_count': row[13],
    #             'catchment_population_cso': row[14],
    #             'operation_status': row[15],
    #             # 'geom': fromstr(f'POINT({row[11]} {row[12]})', srid=4326),
    #             'geom': GEOSGeometry(f'POINT({row[11]} {row[12]})', srid=4326),
    #         })
    #
    # inserted_pks = seeder.execute()
    # logging.info(inserted_pks)


def clear_data():
    """Deletes all the table data"""
    logging.info("Delete facility instances")
    Facility.objects.all().delete()


def run(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    # clear_data()
    if mode == MODE_CLEAR:
        return

    load_facilities()

