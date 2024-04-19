from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photoapp/list.html'
    context_object_name = 'photos'


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photoapp/detail.html'
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'description', 'image']
    template_name = 'photoapp/create.html'
    success_url = reverse_lazy('photo:list')
    def form_valid(self, form):
        form.instance.submitter = self.request.user

        return super().form_valid(form)


class UserIsSubmitter(UserPassesTestMixin):
    # Custom method
    def get_photo(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('pk'))
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('Sorry you are not allowed here')


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(submitter=self.request.user)


# class PhotoUpdateView(UserPassesTestMixin, UpdateView):
class PhotoUpdateView(LoginRequiredMixin, OwnerMixin, UpdateView):
    template_name = 'photoapp/update.html'
    model = Photo
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('photo:list')