import os
from pathlib import Path
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from PIL import Image
from collections import namedtuple


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

    @property
    def thumb(self):
        file_name = Path(self.profile_image.path).name
        url = f"{settings.MEDIA_URL}thumb/{file_name}"
        path = f"{settings.MEDIA_ROOT}/thumb/{file_name}"
        return namedtuple("thumb", ("url", "path"))(url, path)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=image_path, blank=True, default=f'{settings.MEDIA_ROOT}/images/profile_img.jpg')

    def __str__(self):
        return f"profile {self.user}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Profile)
def image_process(sender, instance, created, **kwargs):
    file_name = Path(instance.profile_image.path).name
    img = Image.open(instance.profile_image.path)
    size = img.size
    thm = img.crop((0, 0, size[0], size[0]))
    thm = thm.resize((300, 300))
    thm.save(settings.THUMB_ROOT / file_name)
