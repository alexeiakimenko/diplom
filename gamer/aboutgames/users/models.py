from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')
    favorite_game = models.CharField(max_length=200, blank=True, null=True, verbose_name='Любимая игра')
    favorite_genre = models.CharField(max_length=200, blank=True, null=True, verbose_name='Любимый жанр игр')
    birthday = models.DateField(blank=True, null=True, verbose_name='День рождения')
    username = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ник пользователя')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=200, blank=True, null=True, verbose_name='Email')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = 'Пользователи'
        ordering = ['name']
