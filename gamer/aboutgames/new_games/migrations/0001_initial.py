# Generated by Django 4.2.3 on 2023-08-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='new_game_image/default.jpg', upload_to='new_game_image/%Y/%m/%d')),
                ('video', models.URLField()),
            ],
        ),
    ]
