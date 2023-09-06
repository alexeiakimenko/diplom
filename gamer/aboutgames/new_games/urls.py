from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_games, name='new-games'),
    path('single-new-game/<str:pk>/', views.single_new_game, name='single-new-game'),
    path('new-games-genre/<str:pk>/', views.new_games_genre, name='new-games-genre'),
    path('comment_new_games/<str:pk>/', views.comment_new_games, name='comment_new_games'),
    path('profile_view/<str:name>', views.profile_view, name="profile_view")

]
