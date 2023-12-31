# Generated by Django 4.2.5 on 2023-10-22 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватар')),
                ('favorite_game', models.CharField(blank=True, max_length=200, null=True, verbose_name='Любимая игра')),
                ('favorite_genre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Любимый жанр игр')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('username', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Ник пользователя')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя пользователя')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'пользователя',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['name'],
            },
        ),
    ]
