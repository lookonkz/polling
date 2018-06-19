from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MusicList, HomeViews

app_name = 'musics'
urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
]



