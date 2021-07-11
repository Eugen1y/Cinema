from django import forms

from ticket.models import Ticket
from zal.models import Seans
from zal.services import get_available_seanses


class TicketCreateForm(forms.ModelForm):
    seans = forms.ModelChoiceField(
        queryset=Seans.objects.filter(id__in=get_available_seanses(Seans.objects.all())))

    class Meta:
        model = Ticket
        fields = ['amount', 'seans']

    def get_cleaned_data(self):
        super(TicketCreateForm, self).clean()
        amount = self.cleaned_data.get('amount')
        seans = self.cleaned_data.get('seans')
        return {
            'amount': amount,
            'seans': seans,
        }

