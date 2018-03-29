from django.urls import path
from musics.views import *
from musics.models import LikeDislike, Music

app_name = 'ajax'
urlpatterns = [
    path('music/<int:pk>/like/', VotesView.as_view(model=Music, vote_type=LikeDislike.LIKE),
        name='like'),
    path('music/<int:pk>/dislike/', VotesView.as_view(model=Music, vote_type=LikeDislike.DISLIKE),
        name='dislike'),
]
