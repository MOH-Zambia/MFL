from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from MFL.models import *
from django.shortcuts import render_to_response
from MFL.serializers import FacilitySerializer
from rest_framework import viewsets
from MFL.permissions import IsOwnerOrReadOnly
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


class FacilityDetail(DetailView):
    queryset = Facility.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(FacilityDetail, self).get_context_data(*args, **kwargs)
        return context


class FacilityList(ListView):
    template_name = 'MFL/facility_list.html'
    queryset = Facility.objects.all().order_by('facility_name')

    def get_context_data(self, *args, **kwargs):
        context = super(FacilityList, self).get_context_data(*args, **kwargs)

        query = self.request.GET.get('q')
        page = self.request.GET.get('page')

        if query:
            queryset = Facility.objects.filter(
                Q(facility_name__icontains=query) |
                Q(HMIS_Code__icontains=query)).order_by('facility_name')
            paginator = Paginator(queryset, 2)  # Show 25 contacts per page
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                queryset = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                queryset = paginator.page(paginator.num_pages)
            context['facilities'] = queryset
        else:
            queryset = Facility.objects.all().order_by('facility_name')
            paginator = Paginator(queryset, 2)  # Show 25 contacts per page
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                queryset = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                queryset = paginator.page(paginator.num_pages)
            context['facilities'] = queryset

        return context


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


