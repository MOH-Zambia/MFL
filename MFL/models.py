from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from .utils import unique_slug_generator


class Service(models.Model):
    name = models.CharField(max_length=100)
    # category = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Infrastructure(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Infrastructure"


class Equipment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Equipment"


class OperatingHours(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Operating Hours"


class Province(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class District(models.Model):
    name = models.CharField(max_length=15)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)

    def get_province(self):
        return self.province.name

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Ownership(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Ownership"


class FacilityType(models.Model):
    facility_type = models.CharField(max_length=30)

    def __str__(self):  # __unicode__ on Python 2
        return self.facility_type


class AdministrativeUnit(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class OperationalStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Operational status"

class LabLevel(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural = "Lab Levels"


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


class Facility(models.Model):
    dhis2_uid = models.CharField(max_length=13, null=True, blank=True)
    HMIS_Code = models.CharField(max_length=8)
    facility_name = models.CharField(max_length=30)
    facility_type = models.ForeignKey(FacilityType, on_delete=models.DO_NOTHING)
    operational_status = models.ForeignKey(OperationalStatus, on_delete=models.DO_NOTHING)
    administrative_unit = models.ForeignKey(AdministrativeUnit, on_delete=models.DO_NOTHING)
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
    email = models.EmailField(null=True, blank=True)
    web_address = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    fax = models.CharField(max_length=13, null=True, blank=True)
    street_name = models.CharField(max_length=30, null=True, blank=True)
    street_number = models.CharField(max_length=10, null=True, blank=True)
    area_name = models.CharField(max_length=30, null=True, blank=True)
    postal_address = models.CharField(max_length=10, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    catchment_population = models.IntegerField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    star = models.TextField(max_length=1000, null=True, blank=True)
    # stars = models.ManyToManyField(Star, null=True, blank=True)
    rated = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.TextField(max_length=10, null=True, blank=True)

    def province(self):
        return self.district.province.name

    def __str__(self):  # __unicode__ on Python 2
        return "%s | %s" % (self.HMIS_Code, self.facility_name)

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"

    # objects = FacilityManager()

    def get_absolute_url(self):  # get_absolute_url
        # return f"/facility/{self.slug}"
        return reverse('facility', kwargs={'pk': self.id})

    @property
    def title(self):
        return self.facility_name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.facility_name = instance.facility_name.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    # def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
    #     print('saved')
    #     print(instance.timestamp)
    #     if not instance.slug:
    #         instance.slug = unique_slug_generator(instance)
    #         instance.save()


pre_save.connect(rl_pre_save_receiver, sender=Facility)
