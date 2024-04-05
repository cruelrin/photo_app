from django.shortcuts import render

# Create your views here.
class PhotoListView(ListView):
    model = Photo

    template_name = 'photoapp/list.html'

    context_object_name = 'photos'