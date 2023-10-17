# Generated by Django 4.2.5 on 2023-10-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_games', '0011_alter_comments_favourite_game_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newgame',
            options={'ordering': ['-rating', 'title'], 'verbose_name': 'Анонс игры', 'verbose_name_plural': 'Анонс игр'},
        ),
        migrations.AddField(
            model_name='newgame',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
