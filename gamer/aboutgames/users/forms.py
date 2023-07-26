from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(UserCreationForm):


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2',

        ]

