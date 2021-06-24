from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import *

from zal.models import Zal, Seans, Film


class ZalCreate(LoginRequiredMixin, CreateView):
    model = Zal
    template_name = 'zal-create.html'
    fields = ['name', 'size']
    success_url = '/'


class ZalList(ListView):
    model = Zal
    template_name = 'zal-list.html'
    context_object_name = 'zals'


class SeansCreate(LoginRequiredMixin, CreateView):
    model = Seans
    fields = ['date_start',
              'date_end',
              'film',
              'zal',
              'ticket_amount',
              'price']
    template_name = 'seans-create.html'
    success_url = '/seans/list'


class SeansList(ListView):
    model = Seans
    template_name = 'seans-list.html'
    context_object_name = 'seans'


class FilmAdd(LoginRequiredMixin, CreateView):
    model = Film
    fields = ['name', 'description']
    template_name = 'film-add.html'
    success_url = '/film/list'

class FilmList(ListView):
    model = Film
    template_name = 'film-list.html'
    context_object_name = 'films'
