from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *

from zal.forms import SeansForm
from zal.mixins import StaffRequiredMixin
from zal.models import Zal, Seans, Film


class ZalCreate(StaffRequiredMixin, CreateView):
    model = Zal
    template_name = 'zal-create.html'
    fields = ['name', 'size']
    success_url = '/'


class ZalList(ListView):
    model = Zal
    template_name = 'zal-list.html'
    context_object_name = 'zals'


class SeansCreate(StaffRequiredMixin, CreateView):
    model = Seans
    form_class = SeansForm
    template_name = 'seans-create.html'

    def get_success_url(self):
        return '/seans/list'


class SeansDetail(LoginRequiredMixin, DetailView):
    model = Seans
    template_name = 'seans-detail.html'
    context_object_name = 'tickets'


class SeansList(ListView):
    model = Seans
    template_name = 'seans-list.html'
    context_object_name = 'seans'


class SeansUpdate(StaffRequiredMixin, UpdateView):
    model = Seans
    template_name = 'seans-update.html'
    form_class = SeansForm

    def get_success_url(self):
        return '/seans/list'


class FilmAdd(StaffRequiredMixin, CreateView):
    model = Film
    fields = ['name', 'description']
    template_name = 'film-add.html'
    success_url = '/film/list'


class FilmList(ListView):
    model = Film
    template_name = 'film-list.html'
    context_object_name = 'films'
