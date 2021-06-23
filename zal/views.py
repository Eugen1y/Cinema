from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import *

from zal.models import Zal


class ZalCreate(LoginRequiredMixin, CreateView):
    model = Zal
    template_name = 'zal-create.html'
    fields = ['name', 'size']
    success_url = '/'


class ZalList(ListView):
    model = Zal
    template_name = 'zal-list.html'
    context_object_name = 'zals'
