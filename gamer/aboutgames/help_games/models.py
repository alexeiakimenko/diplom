from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False, verbose_name='Название игры')
    genre = models.CharField(max_length=250, blank=False, null=False, verbose_name='Жанр игры')
    release_date = models.DateField(verbose_name='Дата выхода')
    description = models.TextField(verbose_name='Содержание')
    game_image = models.ImageField(upload_to='game_image/%Y/%m/%d/', blank=True, null=True, verbose_name='Обложка')
    created = models.DateField(verbose_name='Дата написания статьи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'игру'
        verbose_name_plural = 'Игры'
        ordering = ['title']