# Generated by Django 4.2.3 on 2023-08-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['name'], 'verbose_name': 'пользователя', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite_game',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Любимая игра'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite_genre',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Любимый жанр игр'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ник пользователя'),
        ),
    ]