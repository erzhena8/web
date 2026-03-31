import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Asset

@receiver(post_delete, sender=Asset)
def remove_files_on_delete(sender, instance, **kwargs):

    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)