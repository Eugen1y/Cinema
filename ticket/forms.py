from django import forms

from ticket.models import Ticket
from zal.models import Seans
from zal.services import get_available_seanses


class TicketCreateForm(forms.ModelForm):
    amount = forms.DateTimeField

    class Meta:
        model = Ticket
        fields = ['amount','seans']
        seans = get_available_seanses(queryset=Seans.objects.all())
