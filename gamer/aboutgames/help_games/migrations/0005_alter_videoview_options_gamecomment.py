# Generated by Django 4.2.5 on 2023-09-22 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('help_games', '0004_videoview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videoview',
            options={'ordering': ['video_game'], 'verbose_name': 'видео обзор', 'verbose_name_plural': 'Видео Обзоры'},
        ),
        migrations.CreateModel(
            name='GameComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Комментатор')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('comment_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата комментария')),
                ('favourite_game', models.CharField(blank=True, max_length=250, null=True, verbose_name='Любимая игра')),
                ('favourite_genre', models.CharField(blank=True, max_length=250, null=True, verbose_name='Любимый жанр игр')),
                ('game_commented', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='help_games.game', verbose_name='Комментируемая игра')),
            ],
            options={
                'verbose_name': 'комментарий к игре',
                'verbose_name_plural': 'Комментарии к игре',
                'ordering': ['name'],
            },
        ),
    ]