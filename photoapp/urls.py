'''Photoapp URL patterns'''
from django.views.generic import TemplateView
from django.urls import path


app_name = 'photo'

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    # path('', PhotoListView.as_view(), name='list'),
]


