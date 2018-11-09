from django.urls import path
from .views import HomeViews, HomeViews1, TrackDetailView

app_name = 'musics'
urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('link/', HomeViews1.as_view(), name='home3'),
    path('music/<int:pk>/', TrackDetailView.as_view(), name='track')
]



