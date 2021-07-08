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
