from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(pre_save, sender=CustomUser)
def set_unique_uuid(sender, instance, **kwargs):
    if not instance.uuid:
        instance.uuid = instance.generate_uuid()
