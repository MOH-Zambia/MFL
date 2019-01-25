from django.urls import path
from .views import *

urlpatterns = [
    path('features/provinces', feature_provinces, name='provinces'),
    path('features/districts', feature_districts, name='districts'),
    path('features/constituencies', feature_constituencies, name='constituencies'),
    path('features/wards', feature_wards, name='wards'),
]
