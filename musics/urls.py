from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MusicList, register

app_name = 'musics'
urlpatterns = [
    path('', register, name='home'),
    path('musics/', MusicList.as_view(), name='musics'),

]



