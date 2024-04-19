'''Photoapp URL patterns'''
from django.views.generic import TemplateView
from django.urls import path

from photoapp.views import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView

app_name = 'photo'

urlpatterns = [
    path('', PhotoListView.as_view(), name='list'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('photo/create/', PhotoCreateView.as_view(), name='create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),
]


