from django.db import models
from django.contrib.auth.models import User
    
class Location(models.Model):
    name= models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    display_name = models.CharField(max_length=20, null=False, blank=False)
    bio = models.CharField(max_length=80, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    background = models.ImageField(upload_to="backgrounds/", null=True, blank=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.display_name
    

