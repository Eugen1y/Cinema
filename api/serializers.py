from rest_framework import serializers

from ticket.models import Ticket
from zal.models import Zal, Film, Seans


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
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Seans
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
