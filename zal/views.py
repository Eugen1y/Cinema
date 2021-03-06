from datetime import date
from django.views.generic import *

from zal.forms import SeansForm, SeansUpdateForm, ZalUpdateForm
from zal.mixins import StaffRequiredMixin
from zal.models import Zal, SeansGroup, Film, Seans


class ZalCreate(StaffRequiredMixin, CreateView):
    model = Zal
    template_name = 'zal-create.html'
    fields = ['name', 'size']
    success_url = '/'


class ZalList(ListView):
    model = Zal
    template_name = 'zal-list.html'
    context_object_name = 'zals'


class ZalUpdate(StaffRequiredMixin, UpdateView):
    model = Zal
    template_name = 'zal-update.html'
    form_class = ZalUpdateForm

    def get_success_url(self):
        return f'/zal/list'


class ZalDetail(StaffRequiredMixin, DetailView):
    model = Zal
    template_name = 'zal-detail.html'


class SeansCreate(StaffRequiredMixin, CreateView):
    model = SeansGroup
    form_class = SeansForm
    template_name = 'seans-create.html'

    def get_success_url(self):
        return '/seans/list'


class SeansDetail(DetailView):
    model = Seans
    template_name = 'seans-detail.html'
    context_object_name = 'tickets'


class SeansList(ListView):
    model = Seans
    template_name = 'seans-list.html'
    context_object_name = 'seans'

    def get_queryset(self):
        self.queryset = Seans.objects.filter(date_start__gte=date.today()).order_by('date_start')
        return self.queryset


class SeansUpdate(StaffRequiredMixin, UpdateView):
    model = Seans
    template_name = 'seans-update.html'
    form_class = SeansUpdateForm

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


class DateTimeSearch(ListView):
    template_name = 'seans-list.html'
    context_object_name = 'seans'

    def get_queryset(self):
        if self.request.GET.get('date') and self.request.GET.get('time'):
            return Seans.objects.filter(date_start=self.request.GET.get('date'),
                                        time_start__gte=self.request.GET.get('time')).order_by('time_start')
        elif self.request.GET.get('date'):
            return Seans.objects.filter(date_start=self.request.GET.get('date')).order_by('time_start')
        elif self.request.GET.get('price'):
            return Seans.objects.filter(price__gte=self.request.GET.get('price')).order_by('price')
        elif self.request.GET.get('time'):
            return Seans.objects.filter(time_start__gte=self.request.GET.get('time')).order_by('time_start')

    def get_context_data(self, *args, **kwargs):
        context = super(DateTimeSearch, self).get_context_data(*args, **kwargs)
        context['date'] = self.request.GET.get('date')
        context['time'] = self.request.GET.get('time')
        return context
