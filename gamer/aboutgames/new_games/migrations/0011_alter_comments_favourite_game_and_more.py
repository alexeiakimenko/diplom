# Generated by Django 4.2.5 on 2023-09-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_games', '0010_comments_favourite_game_comments_favourite_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='favourite_game',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Любимая игра'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='favourite_genre',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Любимый жанр игр'),
        ),
    ]