from django.db import models
from users.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator


class NewGame(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False, verbose_name='Название игры')
    description = models.TextField(verbose_name='Описание игры')
    genre = models.CharField(max_length=50, blank=True, null=True, verbose_name='Жанр игры')
    genre2 = models.CharField(max_length=50, blank=True, null=True, verbose_name='Жанр игры 2')
    genre3 = models.CharField(max_length=50, blank=True, null=True, verbose_name='Жанр игры 3')
    create = models.DateField(blank=True, null=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='new_game_image/%Y/%m/%d/', default='new_game_image/default.jpg',
                              verbose_name='Картинка')
    video = models.FileField(upload_to='preview/%Y/%m/%d', blank=True, default='preview/default.mp4',
                             verbose_name='Трейлер')
    rating = models.FloatField(default=0, verbose_name='Рейтинг от экспертов на Metarankings.ru')
    rating_site = models.FloatField(default=0, verbose_name='Рейтинг нашего сайта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Анонс игры'
        verbose_name_plural = 'Анонс игр'
        ordering = ['-rating_site', '-rating', 'title']


class Comments(models.Model):
    name = models.CharField(max_length=250, verbose_name='Комментатор')
    avatar = models.ImageField(blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий')
    comment_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата комментария')
    game_commented = models.ForeignKey('NewGame', on_delete=models.PROTECT, verbose_name='Комментируемая игра')
    favourite_game = models.CharField(max_length=250, blank=True, null=True, verbose_name='Любимая игра')
    favourite_genre = models.CharField(max_length=250, blank=True, null=True, verbose_name='Любимый жанр игр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['comment_created']


class NewVoteUser(models.Model):
    evaluation = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(5), MinValueValidator(1)],
                                     verbose_name='Оценка игры пользователем')
    game_evaluation = models.ForeignKey('NewGame', on_delete=models.CASCADE, verbose_name='Для какой игры оценка')
    user_evaluation = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Кто оценивает игру')

    class Meta:
        verbose_name = 'Оценку игры'
        verbose_name_plural = 'Оценка игры'
