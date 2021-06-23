from django.shortcuts import render
from django.views.generic import *

from zal.models import Zal


class ZalCreate(CreateView):
    model = Zal
