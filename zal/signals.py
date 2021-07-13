from django.db.models.signals import post_save
from django.dispatch import receiver

from zal.models import Seans, SeansGroup
from zal.services import daterange


@receiver(post_save, sender=SeansGroup)
def handle_user_post_save_signal(sender, instance, created, *args, **kwargs):

    if created:
        seans_list = daterange(instance.date_start, instance.date_end)
        for seans in seans_list:
            Seans.objects.create(
                seans_group=instance,
                date_start=seans,
                date_end=seans,
                time_start=instance.time_start,
                time_end=instance.time_end,
                film=instance.film,
                zal=instance.zal,
                price=instance.price,

            )
