from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True,null=True)
    favorite_game = models.CharField(max_length=200, blank=True, null=True)
    favorite_genre = models.CharField(max_length=200, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
