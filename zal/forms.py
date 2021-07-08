from django import forms
from django.core.exceptions import ValidationError

from zal.models import SeansGroup, Zal, Film
from zal.services import datetime_validation, tickets_exist


class SeansForm(forms.ModelForm):
    date_start = forms.DateField(widget=forms.SelectDateWidget)
    date_end = forms.DateField(widget=forms.SelectDateWidget)
    time_start = forms.TimeField()
    time_end = forms.TimeField()
    film = Film.objects.all()
    zal = Zal.objects.all()
    price = forms.IntegerField()

    class Meta:
        model = SeansGroup
        fields = ['date_start',
                  'date_end',
                  'time_start',
                  'time_end',
                  'film',
                  'zal',
                  'price']

    def get_cleaned_data(self):
        super(SeansForm, self).clean()
        date_start = self.cleaned_data.get('date_start')
        date_end = self.cleaned_data.get('date_end')
        time_start = self.cleaned_data.get('time_start')
        time_end = self.cleaned_data.get('time_end')
        zal = self.cleaned_data.get('zal')
        seans_id = self.instance.id
        return {'date_start': date_start,
                'date_end': date_end,
                'time_start': time_start,
                'time_end': time_end,
                'zal': zal,
                'id': seans_id
                }

    def save(self, commit=True):
        datetime_validation(self.get_cleaned_data())
        super(SeansForm, self).save()


class SeansUpdateForm(SeansForm):

    def save(self, commit=True):
        if self.instance.get_available_tickets() == self.instance.zal.size:
            super(SeansUpdateForm, self).save()
        else:
            raise ValidationError('Seans already have tickets')


class ZalUpdateForm(forms.ModelForm):
    class Meta:
        model = Zal
        fields = '__all__'

    def get_cleaned_data(self):
        super(ZalUpdateForm, self).clean()
        name = self.cleaned_data.get('name')
        size = self.cleaned_data.get('size')
        return {
            'name': name,
            'size': size,
        }

    def save(self, commit=True):
        try:
            tickets_exist(self.get_cleaned_data())
            super(ZalUpdateForm, self).save()
        except ValidationError:
            ...

