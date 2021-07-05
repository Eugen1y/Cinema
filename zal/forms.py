from django import forms
from zal.models import Seans, Zal, Film
from zal.services import datetime_validation


class SeansForm(forms.ModelForm):
    date_start = forms.DateField(widget=forms.SelectDateWidget)
    date_end = forms.DateField(widget=forms.SelectDateWidget)
    time_start = forms.TimeField()
    time_end = forms.TimeField()
    film = Film.objects.all()
    zal = Zal.objects.all()
    price = forms.IntegerField()

    class Meta:
        model = Seans
        fields = ['date_start',
                  'date_end',
                  'time_start',
                  'time_end',
                  'film',
                  'zal',
                  'price']

    def get_cleaned_data(self, seans_id=None):
        super(SeansForm, self).clean()
        date_start = self.cleaned_data.get('date_start')
        date_end = self.cleaned_data.get('date_end')
        time_start = self.cleaned_data.get('time_start')
        time_end = self.cleaned_data.get('time_end')
        zal = self.cleaned_data.get('zal')
        zal_objects = Seans.objects.filter(zal=zal).exclude(id=seans_id)

        return {'date_start': date_start,
                'date_end': date_end,
                'time_start': time_start,
                'time_end': time_end,
                'zal_objects': zal_objects,
                'zal': zal
                }

    def save(self, commit=True):
        seans = self.get_cleaned_data()
        self.instance.date_start = seans['date_start']
        self.instance.date_end = seans['date_end']
        self.instance.time_start = seans['time_start']
        self.instance.time_end = seans['time_end']
        self.instance.zal = seans['zal']
        datetime_validation(self)
        super(SeansForm, self).save()


class SeansUpdateForm(SeansForm):
    pass
