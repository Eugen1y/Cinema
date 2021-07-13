from django.core.exceptions import ValidationError


def available_tickets(data):
    seans = data.get('seans')
    available_tickets = seans.get_available_tickets()
    if available_tickets < data['amount']:
        raise ValidationError(
            f'U select too much tickets.Available - {available_tickets}')
