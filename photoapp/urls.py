'''Photoapp URL patterns'''
from django.views.generic import TemplateView
from django.urls import path

from photoapp.views import PhotoListView

app_name = 'photo'

urlpatterns = [
    path('', PhotoListView.as_view(), name='list'),
]


