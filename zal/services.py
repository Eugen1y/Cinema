from django.apps import apps


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
