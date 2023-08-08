from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_games, name='new-games'),
    path('single-new-game/<str:pk>/', views.single_new_game, name='single-new-game'),
]
