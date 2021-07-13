from django.db import models
from django.urls import reverse_lazy

from zal.models import Seans


class Ticket(models.Model):
    seans = models.ForeignKey(Seans, related_name='tickets', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def get_absolute_url(self):
        return reverse_lazy('ticket-detail', kwargs={"pk": self.id})

    def __str__(self):
        return f'{self.seans}, {self.amount}'

    def __repr__(self):
        return f"<{self.__class__.__name__} pk={self.pk} ('{self}')>"

    def get_total(self):
        return self.seans.price * self.amount
