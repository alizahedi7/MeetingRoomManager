from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    USER_ROLES = (
        ('normal', 'Normal'),
        ('manager', 'Manager'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=30)
    email_confirmed = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='normal')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
