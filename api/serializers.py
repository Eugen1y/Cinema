from django.contrib.auth.models import User
from rest_framework import serializers

from ticket.models import Ticket
from zal.models import Zal, Film, Seans
from zal.services import datetime_validation


class ZalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Zal
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Film
        fields = '__all__'


class SeansSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    tickets = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Seans
        fields = '__all__'

    validators = [datetime_validation]


class TicketSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
