from django.urls import path
from . import views

urlpatterns = [
    path('', views.help_games, name='help_games'),
    path('single_game/<int:pk>', views.single_game, name='single_game'),
    path('hint_game/<str:title>', views.hint_game, name='hint_game'),
    path('video_view_game/<str:title>', views.video_view_game, name='video_view_game'),
    path('help_games_genre/<str:title>', views.help_games_genre, name='help_games_genre'),
    path('comment_games/<int:pk>/', views.comment_games, name='comment_games'),
    path('search_game/', views.search_game, name='search_game'),

]
