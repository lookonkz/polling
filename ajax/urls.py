from django.urls import path
from musics.views import *
from musics.models import LikeDislike, MusicClip, MusicTrack
from allauth.account.views import LogoutView

app_name = 'ajax'
urlpatterns = [
    path('alogout/', LogoutView.as_view(), name='account_logout'),
    path('music/<int:pk>/like/', VotesView.as_view(model=MusicClip, vote_type=LikeDislike.LIKE),
        name='like'),
    path('music/<int:pk>/dislike/', VotesView.as_view(model=MusicClip, vote_type=LikeDislike.DISLIKE),
        name='dislike'),
    path('musictrack/<int:pk>/like/', VotesView.as_view(model=MusicTrack, vote_type=LikeDislike.LIKE),
        name='musictrack_like'),
    path('musictrack/<int:pk>/dislike/', VotesView.as_view(model=MusicTrack, vote_type=LikeDislike.DISLIKE),
        name='musictrack_dislike'),
]
