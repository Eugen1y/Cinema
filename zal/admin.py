from django.contrib import admin

from zal.models import Zal


@admin.register(Zal)
class ZalAdmin(admin.ModelAdmin):
    fields = ['name', 'amount_mest']
    list_display = ['name', 'amount_mest']



