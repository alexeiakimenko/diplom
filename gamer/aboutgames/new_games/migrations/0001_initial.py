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
            name='NewGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название игры')),
                ('description', models.TextField(verbose_name='Описание игры')),
                ('genre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Жанр игры')),
                ('create', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('image', models.ImageField(default='new_game_image/default.jpg', upload_to='new_game_image/%Y/%m/%d/', verbose_name='Картинка')),
                ('video', models.FileField(blank=True, default='preview/default.mp4', upload_to='preview/%Y/%m/%d', verbose_name='Трейлер')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг от экспертов на Metarankings.ru')),
                ('rating_site', models.FloatField(default=0, verbose_name='Рейтинг нашего сайта')),
            ],
            options={
                'verbose_name': 'Анонс игры',
                'verbose_name_plural': 'Анонс игр',
                'ordering': ['-rating_site', '-rating', 'title'],
            },
        ),
        migrations.CreateModel(
            name='NewVoteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Оценка игры пользователем')),
                ('game_evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_games.newgame', verbose_name='Для какой игры оценка')),
                ('user_evaluation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Кто оценивает игру')),
            ],
            options={
                'verbose_name': 'Оценку игры',
                'verbose_name_plural': 'Оценка игры',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Комментатор')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('comment_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата комментария')),
                ('favourite_game', models.CharField(blank=True, max_length=250, null=True, verbose_name='Любимая игра')),
                ('favourite_genre', models.CharField(blank=True, max_length=250, null=True, verbose_name='Любимый жанр игр')),
                ('game_commented', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='new_games.newgame', verbose_name='Комментируемая игра')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['comment_created'],
            },
        ),
    ]
