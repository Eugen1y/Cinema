from django.db import models
from zal.services import get_available


class Zal(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(default=20,
                               verbose_name='Количество мест'
                               )

    def __str__(self):
        return self.name

    def __repr__(self):

        return f"<Zal {self}>"

class Film(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255,
                                   verbose_name='Описание'
                                   )

    def __str__(self):
        return self.name


class SeansGroup(models.Model):
    date_start = models.DateField(default=0)
    date_end = models.DateField(default=0)
    time_start = models.TimeField(default=0)
    time_end = models.TimeField(default=0)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1)
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    price = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.film}{self.date_start} {self.time_start}'


class Seans(models.Model):
    seans_group = models.ForeignKey(SeansGroup,related_name='seanses', on_delete=models.CASCADE)
    date_start = models.DateField(default=0)
    date_end = models.DateField(default=0)
    time_start = models.TimeField(default=0)
    time_end = models.TimeField(default=0)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1)
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    price = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.film}{self.date_start} {self.time_start}'

    def get_available_tickets(self):
        return get_available(self)
