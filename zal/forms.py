from django import forms
from django.core.exceptions import ValidationError

from zal.models import Seans, Zal, Film


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

    def time_valid(self):
        super(SeansForm, self).clean()
        date_start = self.cleaned_data.get('date_start')
        date_end = self.cleaned_data.get('date_end')
        time_start = self.cleaned_data.get('time_start')
        time_end = self.cleaned_data.get('time_end')
        zal = self.cleaned_data.get('zal')
        zal_objects = Seans.objects.filter(zal=zal)
        if zal_objects:
            for obj in zal_objects:
                if (obj.date_start <= date_start <= obj.date_end and obj.time_start <= time_start <= obj.time_end) or (
                        obj.date_end >= date_end >= obj.date_start and obj.time_end >= time_end >= obj.time_start):
                    raise ValidationError(message='Invalid date or time')
                else:
                    continue

    def save(self, commit=True):
        super(SeansForm, self).clean()
        date_start = self.cleaned_data.get('date_start')
        date_end = self.cleaned_data.get('date_end')
        time_start = self.cleaned_data.get('time_start')
        time_end = self.cleaned_data.get('time_end')
        zal = self.cleaned_data.get('zal')
        self.instance.date_start = date_start
        self.instance.date_end = date_end
        self.instance.time_start = time_start
        self.instance.time_end = time_end
        self.instance.zal = zal
        self.time_valid()
        super(SeansForm, self).save()
