from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ModelForm
from django.contrib.auth.models import User


class FullForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'name',
            'email',
            'avatar',
            'favorite_game',
            'favorite_genre',
            'birthday',

        ]
        labels = {
            'avatar': 'Ваше фото или аватар',
            'favorite_game': 'Любимая игра',
            'favorite_genre': 'Любимый игровой жанр',
            'birthday': 'Дата рождения',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2',

        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
