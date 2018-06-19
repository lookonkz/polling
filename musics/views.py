from django.shortcuts import render, redirect
import json
from django.views import View
from django.contrib.contenttypes.models import ContentType
from .models import LikeDislike, MusicClip, Category
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import MusicTrack
from django.http import JsonResponse


class VotesView(View):
    model = None  # Модель данных - Статьи или Комментарии
    vote_type = None  # Тип комментария Like/Dislike

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id,
                                                  user=request.user)

            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        obj.reiting =int(obj.votes.likes().count())
        obj.save()

        return JsonResponse({
                "result": result,
                "like_count": obj.votes.likes().count(),
                # "dislike_count": obj.votes.dislikes().count(),
            })


class MusicList(ListView):
    model = MusicClip
    context_object_name = 'music_list'
    template_name = 'musics/music_list.html'
    paginate_by = 50


class HomeViews(TemplateView):
    template_name = 'musics/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['music_list'] = MusicClip.objects.all()[:10]
        context['category_list'] = Category.objects.all().values('id', 'name')
        context['category'] = Category.objects.all()
        return context
