from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MusicList

app_name = 'musics'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='account/login.html'), name='home'),
    path('musics/', MusicList.as_view(), name='musics'),

]



