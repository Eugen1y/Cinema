from django.apps import apps
from django.core.exceptions import ValidationError


def get_available(seans):
    model = apps.get_model('ticket', 'Ticket')
    seans_tickets = model.objects.filter(seans=seans)
    place_count = 0
    for ticket in seans_tickets:
        place_count += ticket.amount

    return seans.zal.size - place_count


def get_available_seanses(queryset):
    available_seanses = []
    seanses_id = []
    x = 0
    for seans in queryset:
        if get_available(seans) != 0:
            available_seanses.append(seans)
    for seans in available_seanses:
        seanses_id.append(seans.id)
        x += 1
    return seanses_id


def datetime_validation(data):
    date_start = data['date_start']
    date_end = data['date_end']
    time_start = data['time_start']
    time_end = data['time_end']
    zal_objects = data['zal_objects']
    if zal_objects:
        for obj in zal_objects:
            if obj.date_start <= date_start <= obj.date_end or obj.date_end >= date_end >= obj.date_start:
                if obj.time_start <= time_start <= obj.time_end:
                    raise ValidationError(message='Invalid date or time')
                elif time_start <= obj.time_start and time_end >= obj.time_end or time_end <= obj.time_end:
                    raise ValidationError(message='Invalid date or time')
            elif date_start <= obj.date_start and \
                    (obj.date_end >= date_end >= obj.date_start or date_end >= obj.date_end):
                if obj.time_start <= time_start <= obj.time_end:
                    raise ValidationError(message='Invalid date or time')
                elif time_start <= obj.time_start and time_end >= obj.time_end or time_end <= obj.time_end:
                    raise ValidationError(message='Invalid date or time')
