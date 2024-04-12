from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photoapp/list.html'
    context_object_name = 'photos'