from django.db import models
from django.urls import reverse_lazy

from zal.models import Seans


class Ticket(models.Model):
    seans = models.ForeignKey(Seans, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def get_absolute_url(self):
        """Return an absolute URLs for an instance"""

        return reverse_lazy('ticket-detail', kwargs={"pk": self.pk})
