from django.db import models
from django.contrib.gis.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .utils import unique_slug_generator
from geography.models import District, Constituency, Ward, LocationType


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Service Categories"


class Service(models.Model):
    name = models.CharField(max_length=100)
    # category = models.CharField(max_length=100)
    category = models.ForeignKey(ServiceCategory, on_delete=models.DO_NOTHING)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Infrastructure(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Infrastructure"


class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Equipment"


class OperatingHours(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Operating Hours"


class Ownership(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Ownership"


class FacilityType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Facility Types"


class AdministrativeUnit(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class OperationStatus(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Operation Status"


class LabLevel(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


# class FacilityQuerySet(models.query.QuerySet):
#     def search(self, query):
#         if query:
#             query = query.strip()
#             return self.filter(
#                 Q(facility_name__icontains=query) |
#                 Q(HMISCode__icontains=query)
#             ).distinct()
#         return self
#
#
# class FacilityManager(models.Manager):
#     def get_queryset(self):
#         return FacilityQuerySet(self.model, using=self._db)
#
#     def search(self, query):
#         return self.get_queryset().search(query)


class SearchManager(models.Manager):
    def search(self, **kwargs):
        query_string = ''
        qs = self.all()

        if kwargs.get('form_data').get('name', ''):
            qs = qs.filter(name__icontains=kwargs['form_data']['name'])
            query_string += '&name=' + kwargs['form_data']['name']
        if kwargs.get('form_data').get('facility_type', []):
            qs = qs.filter(facility_type=kwargs['form_data']['facility_type'])
            query_string += '&facility_type=' + kwargs['form_data']['facility_type']
        if kwargs.get('form_data').get('operation_status', []):
            qs = qs.filter(operation_status=kwargs['form_data']['operation_status'])
            query_string += '&operation_status=' + kwargs['form_data']['operation_status']
        if kwargs.get('form_data').get('ownership', []):
            qs = qs.filter(ownership=kwargs['form_data']['ownership'])
            query_string += '&ownership=' + kwargs['form_data']['ownership']

        return {
            'query_set': qs,
            'query_string': query_string
        }


class Facility(models.Model):
    DHIS2_UID = models.CharField(max_length=13, null=True, blank=True)
    HMIS_code = models.CharField(max_length=10, null=True, blank=True)
    smartcare_GUID = models.CharField(max_length=36, null=True, blank=True)
    eLMIS_ID = models.CharField(max_length=13, null=True, blank=True)
    iHRIS_ID = models.CharField(max_length=13, null=True, blank=True)
    name = models.CharField(max_length=100)
    facility_type = models.ForeignKey(FacilityType, on_delete=models.DO_NOTHING)
    operation_status = models.ForeignKey(OperationStatus, on_delete=models.DO_NOTHING, default=1)
    administrative_unit = models.ForeignKey(AdministrativeUnit, on_delete=models.DO_NOTHING, null=True, blank=True)
    ownership = models.ForeignKey(Ownership, on_delete=models.DO_NOTHING)
    services = models.ManyToManyField(Service)
    lab_level = models.ManyToManyField(LabLevel)
    operating_hours = models.ManyToManyField(OperatingHours)
    infrastructure = models.ManyToManyField(Infrastructure, blank=True)
    equipment = models.ManyToManyField(Equipment, blank=True)
    number_of_beds = models.IntegerField(null=True, blank=True)
    number_of_cots = models.IntegerField(null=True, blank=True)
    number_of_nurses = models.IntegerField(null=True, blank=True)
    number_of_doctors = models.IntegerField(null=True, blank=True)
    address_line1 = models.CharField(_('Address 1'), max_length=60, null=True, blank=True, help_text='Street addrees, '
                                                                                                     'P.O Box')
    address_line2 = models.CharField(_('Address 2'), max_length=60, null=True, blank=True, help_text='Apartment, '
                                                                                                     'suite, unit, '
                                                                                                     'building, '
                                                                                                     'floor, etc')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    constituency = models.ForeignKey(Constituency, on_delete=models.DO_NOTHING, null=True, blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.DO_NOTHING, null=True, blank=True)
    postal_address = models.CharField(_('Postal box'), max_length=25, null=True, blank=True, help_text='Postal address')
    location_type = models.ForeignKey(LocationType, on_delete=models.DO_NOTHING, null=True, blank=True)
    web_address = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    fax = models.CharField(max_length=13, null=True, blank=True)
    catchment_population_head_count = models.IntegerField(null=True, blank=True)
    catchment_population_cso = models.IntegerField(null=True, blank=True)
    star = models.TextField(max_length=1000, null=True, blank=True)
    # stars = models.ManyToManyField(Star, null=True, blank=True)
    rated = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.TextField(max_length=10, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    geom = models.PointField(srid=4326, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(max_length=254, null=True, blank=True)

    def province(self):
        return self.district.province.name

    def __str__(self):  # __unicode__ on Python 2
        return "%s | %s" % (self.HMIS_code, self.name)

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"

    # objects = FacilityManager()

    def get_absolute_url(self):  # get_absolute_url
        # return f"/facility/{self.slug}"
        return reverse('facility', kwargs={'pk': self.id})

    @property
    def title(self):
        return self.name

    objects = SearchManager()


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.facility_name = instance.name.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    # def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
    #     print('saved')
    #     print(instance.timestamp)
    #     if not instance.slug:
    #         instance.slug = unique_slug_generator(instance)
    #         instance.save()


pre_save.connect(rl_pre_save_receiver, sender=Facility)


