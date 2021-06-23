from django.db import models


class Zal(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(default=20, verbose_name='Количество мест')


class Seans(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=2, decimal_places=2, default=10)

