from django.contrib.auth.mixins import LoginRequiredMixin
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


class SeansCreate(StaffRequiredMixin, CreateView):
    model = SeansGroup
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
    # paginate_by = 10


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


class ZalUpdate(StaffRequiredMixin, UpdateView):
    model = Zal
    template_name = 'zal-update.html'
    form_class = ZalUpdateForm

    def get_success_url(self):
        return f'/zal/list'


class ZalDetail(LoginRequiredMixin, DetailView):
    model = Zal
    template_name = 'zal-detail.html'


class DateTimeSearch(ListView):
    template_name = 'seans-list.html'
    context_object_name = 'seans'

    def get_queryset(self):
        if self.request.GET.get('date') and self.request.GET.get('time'):
            return Seans.objects.filter(date_start=self.request.GET.get('date'),
                                        time_start__gte=self.request.GET.get('time'))
        if self.request.GET.get('date'):
            return Seans.objects.filter(date_start=self.request.GET.get('date'))
        else:
            return Seans.objects.filter(
                time_start__gte=self.request.GET.get('time'))

    def get_context_data(self, *args, **kwargs):
        context = super(DateTimeSearch, self).get_context_data(*args, **kwargs)
        context['date'] = self.request.GET.get('date')
        context['time'] = self.request.GET.get('time')
        return context
