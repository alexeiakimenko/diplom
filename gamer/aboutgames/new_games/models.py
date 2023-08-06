from django.db import models




class NewGame(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='new_game_image/%Y/%m/%d', default='new_game_image/background.jpg')
    video = models.URLField()
