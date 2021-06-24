from django.db import models


class Zal(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(default=20,
                               verbose_name='Количество мест'
                               )

    def __str__(self):
        return  self.name


class Film(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255,
                                   verbose_name='Описание'
                                   )

    def __str__(self):
        return self.name


class Seans(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1)
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    ticket_amount = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=2, decimal_places=2, default=10)
