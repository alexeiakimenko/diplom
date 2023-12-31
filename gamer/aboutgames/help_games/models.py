from django.db import models
from users.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator


class Game(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False, verbose_name='Название игры')
    genre = models.CharField(max_length=250, blank=False, null=False, verbose_name='Жанр игры')
    genre2 = models.CharField(max_length=250, blank=True, null=True, verbose_name='Жанр игры 2')
    genre3 = models.CharField(max_length=250, blank=True, null=True, verbose_name='Жанр игры 3')
    release_date = models.DateField(verbose_name='Дата выхода')
    description = models.TextField(verbose_name='Содержание')
    game_image = models.ImageField(upload_to='game_image/%Y/%m/%d/', blank=True, null=True, verbose_name='Обложка')
    created = models.DateField(verbose_name='Дата написания статьи')
    rating = models.FloatField(default=0, verbose_name='Рейтинг игроков от Metarankings.ru')
    rating_site = models.FloatField(default=0, verbose_name='Рейтинг нашего сайта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'игру'
        verbose_name_plural = 'Игры'
        ordering = ['-rating_site', '-rating', 'title']


class Hint(models.Model):
    hint_title = models.CharField(max_length=200, verbose_name='Название подсказки')
    hint_description = models.TextField('Описание подсказки')
    hint_game = models.ForeignKey('Game', on_delete=models.CASCADE, verbose_name='Для какой игры подсказка')

    def __str__(self):
        return self.hint_title

    class Meta:
        verbose_name = 'подсказку'
        verbose_name_plural = 'Подсказки'
        ordering = ['hint_game']


class VideoView(models.Model):
    video_title = models.CharField(max_length=200, verbose_name='Название видео обзора')
    video_description = models.URLField(max_length=300, verbose_name='Видео обзор')
    video_game = models.ForeignKey('Game', on_delete=models.CASCADE, verbose_name='Для какой игры обзор')

    def __str__(self):
        return self.video_title

    class Meta:
        verbose_name = 'видео обзор'
        verbose_name_plural = 'Видео Обзоры'
        ordering = ['video_game']


class GameComment(models.Model):
    name = models.CharField(max_length=250, verbose_name='Комментатор')
    avatar = models.ImageField(blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий')
    comment_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата комментария')
    comment_game = models.ForeignKey('Game', on_delete=models.PROTECT, verbose_name='Комментируемая игра')
    favourite_game = models.CharField(max_length=250, blank=True, null=True, verbose_name='Любимая игра')
    favourite_genre = models.CharField(max_length=250, blank=True, null=True, verbose_name='Любимый жанр игр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'комментарий к игре'
        verbose_name_plural = 'Комментарии к игре'
        ordering = ['-comment_created']


class VoteUser(models.Model):
    evaluation = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(5), MinValueValidator(5)],
                                     verbose_name='Оценка игры пользователем')
    game_evaluation = models.ForeignKey('Game', on_delete=models.CASCADE, verbose_name='Для какой игры оценка')
    user_evaluation = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Кто оценивает игру')

    class Meta:
        verbose_name = 'Оценку игры'
        verbose_name_plural = 'Оценка игры'
