from django.db import models


class Zal(models.Model):
    name = models.CharField(max_length=255)
    amount_mest = models.IntegerField(default=20)



class Mesto(models.Model):
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    price = models.IntegerField(default=10)


class Seans(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    mesto = models.ForeignKey(Mesto, on_delete=models.CASCADE)
