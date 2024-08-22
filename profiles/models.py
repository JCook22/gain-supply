from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Model for creating user profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=60, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username

    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ 
    Updates the users profile or creates one if one doesn't exist
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class EmployeeProfile(models.Model):
    """
    Model for employee profiles, which are only accessible in admin.
    This is for internal users only should they need to contact other staff.
    """
    full_name = models.CharField(max_length=50, null=False, blank=False)
    role = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    telephone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=60, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.full_name