import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class Profile(models.Model):
    def image_path(self, filename):
        name_parts = filename.split(".")
        ext = None
        if len(name_parts) > 1:
            ext = name_parts[-1]
        new_filename = os.urandom(24).hex()
        if ext is not None:
            new_filename = f"{new_filename}.{ext}"

        curr_dt = datetime.utcnow()
        new_filename = curr_dt.strftime(f"%Y/%m/%d/%H%M%S_{new_filename}")
        return new_filename

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=image_path, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
