from django.contrib import admin

from zal.models import Zal


@admin.register(Zal)
class ZalAdmin(admin.ModelAdmin):
    fields = ['name', 'size']
    list_display = ['name', 'size']



