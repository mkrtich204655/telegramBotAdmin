from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import CustomUser, Rating, History


@receiver(pre_save, sender=CustomUser)
def set_unique_uuid(sender, instance, **kwargs):
    if not instance.uuid:
        instance.uuid = instance.generate_uuid()


@receiver(post_save, sender=CustomUser)
def creat_rating(sender, instance, **kwargs):
    if not Rating.objects.filter(user=instance).exists():
        Rating.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def creat_history(sender, instance, **kwargs):
    if not History.objects.filter(user=instance).exists():
        History.objects.create(user=instance)
