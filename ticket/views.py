from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from ticket.forms import TicketCreateForm
from ticket.models import Ticket
from ticket.services import available_tickets


class TicketCreate(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'ticket-create.html'
    form_class = TicketCreateForm

    def form_valid(self, form):
        available_tickets(form.get_cleaned_data())
        form.instance.user = self.request.user
        return super(TicketCreate, self).form_valid(form)


class TicketList(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'ticket-list.html'
    context_object_name = 'ticket_list'

    def get_queryset(self):
        queryset = super(TicketList, self).get_queryset()
        return queryset.filter(user=self.request.user)

    def total_spend_money(self, queryset):
        money = 0
        for ticket in queryset:
            money += ticket.get_total()
        return money

class TicketDetail(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'ticket-detail.html'
