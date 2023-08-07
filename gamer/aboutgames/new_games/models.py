from django.db import models


class NewGame(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='new_game_image/%Y/%m/%d/', default='new_game_image/default.jpg')
    video = models.FileField(upload_to='preview/%Y/%m/%d', blank=True,default='preview/default.mp4')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
