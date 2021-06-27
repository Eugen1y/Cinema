from django.db import models


class Zal(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(default=20,
                               verbose_name='Количество мест'
                               )

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255,
                                   verbose_name='Описание'
                                   )

    def __str__(self):
        return self.name


class Seans(models.Model):
    date_start = models.DateField(default=0)
    date_end = models.DateField(default=0)
    time_start = models.TimeField(default=0)
    time_end = models.TimeField(default=0)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1)
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    price = models.IntegerField(default=10)






class Ticket(models.Model):
    seans = models.OneToOneField(Seans, on_delete=models.DO_NOTHING)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

