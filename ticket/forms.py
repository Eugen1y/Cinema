from django import forms

from ticket.models import Ticket
from zal.models import SeansGroup
from zal.services import get_available_seanses


class TicketCreateForm(forms.ModelForm):
    #seans = forms.ModelChoiceField(
        #queryset=SeansGroup.objects.filter(id__in=get_available_seanses(SeansGroup.objects.all())))

    class Meta:
        model = Ticket
        fields = ['amount', 'seans']
