from django.db.models import Q
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize
from MFL.serializers import FacilitySerializer, GeoFacilitySerializer
from rest_framework import viewsets
from MFL.permissions import IsOwnerOrReadOnly
from MFL.models import *
from MFL.forms import SearchForm


class FacilityDetail(DetailView):
    queryset = Facility.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(FacilityDetail, self).get_context_data(*args, **kwargs)
        return context


class FacilityList(ListView):
    template_name = 'MFL/facility_list.html'
    queryset = Facility.objects.all().order_by('name')

    def get_context_data(self, *args, **kwargs):
        context = super(FacilityList, self).get_context_data(*args, **kwargs)

        query = self.request.GET.get('name')
        page = self.request.GET.get('page')
        form = SearchForm(self.request.GET)

        if form.is_valid():
            search_result = Facility.objects.search(form_data=self.request.GET)
            queryset = search_result['query_set'].order_by('name')
            count = queryset.count()
            paginator = Paginator(queryset, 20)  # Show 20 facilities per page
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                queryset = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                queryset = paginator.page(paginator.num_pages)
            context = {
                'form': form,
                'facilities': queryset,
                'query_string': search_result['query_string'],
                'count': count
            }
        else:
            if query:
                queryset = Facility.objects.filter(
                    Q(name__icontains=query) |
                    Q(HMIS_Code__icontains=query)).order_by('name')
                count = queryset.count()
                paginator = Paginator(queryset, 20)  # Show 20 facilities per page
                try:
                    queryset = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    queryset = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    queryset = paginator.page(paginator.num_pages)
                context = {
                    'form': form,
                    'facilities': queryset,
                    'count': count,
                }
            else:
                queryset = Facility.objects.all().order_by('name')
                count = queryset.count()
                paginator = Paginator(queryset, 20)  # Show 20 facilities per page
                try:
                    queryset = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    queryset = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    queryset = paginator.page(paginator.num_pages)
                context = {
                    'form': form,
                    'facilities': queryset,
                    'count': count,
                }
        return context


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class FeatureFacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = GeoFacilitySerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


def feature_facilities(request):
    facilities = serialize('geojson', Facility.objects.all(), fields=('HMIS_Code', 'name', 'facility_type',
                                                                      'operation_status', 'ownership', 'services',
                                                                      'latitude', 'longitude', 'geom'))
    return HttpResponse(facilities, content_type='json')


class MapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        # context['num_facilities'] = Facility.objects.all().count()
        context['num_facilities'] = Facility.objects.filter(~Q(facility_type=8)).count()
        context['num_hospitals'] = Facility.objects.filter(facility_type__in=[4, 5, 6]).count()

        context['num_UHC'] = Facility.objects.filter(facility_type__id=3).count()
        context['num_RHC'] = Facility.objects.filter(facility_type__id=2).count()
        context['num_HP'] = Facility.objects.filter(facility_type__id=1).count()
        context['num_private'] = Facility.objects.filter(facility_type__id=8).count()

        return context
