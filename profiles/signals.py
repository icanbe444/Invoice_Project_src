from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User


"""
This is to allow profile be automatically created when a user is created 
signals in django are used to communicate between models
steps to achieve this:
step 1- create signals.py
step 2- register signal in the apps.py 
    def ready(self):
        import profiles.signals

step 3- go to init.py and add "default_app_cofig = 'profiles.apps.ProfilesConfig'
the "ProfilesConfig" is imported from ProfilesConfig class in apps.py


"""

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


