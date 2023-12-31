# Generated by Django 4.2.5 on 2023-10-22 17:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название игры')),
                ('genre', models.CharField(max_length=250, verbose_name='Жанр игры')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
                ('description', models.TextField(verbose_name='Содержание')),
                ('game_image', models.ImageField(blank=True, null=True, upload_to='game_image/%Y/%m/%d/', verbose_name='Обложка')),
                ('created', models.DateField(verbose_name='Дата написания статьи')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг игроков от Metarankings.ru')),
                ('rating_site', models.FloatField(default=0, verbose_name='Рейтинг нашего сайта')),
            ],
            options={
                'verbose_name': 'игру',
                'verbose_name_plural': 'Игры',
                'ordering': ['-rating_site', '-rating', 'title'],
            },
        ),
        migrations.CreateModel(
            name='VoteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(5)], verbose_name='Оценка игры пользователем')),
                ('game_evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_games.game', verbose_name='Для какой игры оценка')),
                ('user_evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Кто оценивает игру')),
            ],
            options={
                'verbose_name': 'Оценку игры',
                'verbose_name_plural': 'Оценка игры',
            },
        ),
        migrations.CreateModel(
            name='VideoView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=200, verbose_name='Название видео обзора')),
                ('video_description', models.URLField(max_length=300, verbose_name='Видео обзор')),
                ('video_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_games.game', verbose_name='Для какой игры обзор')),
            ],
            options={
                'verbose_name': 'видео обзор',
                'verbose_name_plural': 'Видео Обзоры',
                'ordering': ['video_game'],
            },
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint_title', models.CharField(max_length=200, verbose_name='Название подсказки')),
                ('hint_description', models.TextField(verbose_name='Описание подсказки')),
                ('hint_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_games.game', verbose_name='Для какой игры подсказка')),
            ],
            options={
                'verbose_name': 'подсказку',
                'verbose_name_plural': 'Подсказки',
                'ordering': ['hint_game'],
            },
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
                ('comment_game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='help_games.game', verbose_name='Комментируемая игра')),
            ],
            options={
                'verbose_name': 'комментарий к игре',
                'verbose_name_plural': 'Комментарии к игре',
                'ordering': ['-comment_created'],
            },
        ),
    ]
