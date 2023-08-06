from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_games, name='new-games')
]
