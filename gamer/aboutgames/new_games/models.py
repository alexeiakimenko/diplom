from django.db import models



class NewGame(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False, verbose_name='Название игры')
    description = models.TextField(verbose_name='Описание игры')
    genre = models.CharField(max_length=50, blank=True, null=True, verbose_name='Жанр игры')
    create = models.DateField(blank=True, null=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='new_game_image/%Y/%m/%d/', default='new_game_image/default.jpg',
                              verbose_name='Картинка')
    video = models.FileField(upload_to='preview/%Y/%m/%d', blank=True, default='preview/default.mp4',
                             verbose_name='Трейлер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Анонс игры'
        verbose_name_plural = 'Анонс игр'
        ordering = ['title']


class Comments(models.Model):
    name = models.CharField(max_length=250, verbose_name='Комментатор')
    comment = models.TextField(verbose_name='Комментарий')
    comment_created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата комментария')
    game_commented = models.ForeignKey('NewGame', on_delete=models.PROTECT, verbose_name='Комментируемая игра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-comment_created']
