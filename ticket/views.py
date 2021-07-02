from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import *

from ticket.forms import TicketCreateForm
from ticket.models import Ticket


class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'ticket-create.html'
    form_class = TicketCreateForm

    def form_valid(self, form):
        available_tickets = form.instance.seans.get_available_tickets()
        if available_tickets < form.cleaned_data['amount']:
            raise ArithmeticError(f'Amount should be in range 1 - {available_tickets}')
        form.instance.user = self.request.user
        return super(TicketCreate, self).form_valid(form)


class TicketList(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket-list.html'
    context_object_name = 'ticket_list'

    def get_queryset(self):
        queryset = super(TicketList, self).get_queryset()

        return queryset.filter(user=self.request.user)


class TicketDetail(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'ticket-detail.html'
