from django.urls import path
from . import views

urlpatterns = [
    path('',views.help_games,name='help_games')
]