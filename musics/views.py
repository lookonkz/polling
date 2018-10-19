from django.views import View
from django.contrib.contenttypes.models import ContentType
from .models import LikeDislike, MusicClip, Category, MusicTrack
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
# from django_filters.views import FilterView
# from .filters import MusicTrackFilter


@method_decorator(cache_page(60 * 50), name='dispatch')
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
                obj.reiting = int(obj.reiting) + 1
                obj.save()
            # elif likedislike.vote is self.vote_type:
            #     likedislike.vote = self.vote_type
            #     likedislike.save(update_fields=['vote'])
            #     result = True
            #     c.reiting = int(c.reiting) - 1
            #     c.save()
            else:
                likedislike.delete()
                obj.reiting = int(obj.reiting) - 1
                obj.save()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        obj.reiting =int(obj.votes.likes().count())
        obj.save()

        return JsonResponse({
                "result": result,
                "like_count": obj.reiting,
                "dislike_count": obj.reiting,
            })


class MusicList(ListView):
    model = MusicClip
    context_object_name = 'music_list'
    template_name = 'musics/music_list.html'
    paginate_by = 50


class HomeViews(ListView):
    template_name = 'musics/home2.html'
    model = MusicTrack
    context_object_name = 'music_trakss'
    paginate_by = 25
    # filterset_class = MusicTrackFilter

    def get_queryset(self):
        qs = self.model.objects.all().order_by('-reiting', 'id').distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('page'):
            if int(self.request.GET.get('page')) > 1:
                page = 25 * int(self.request.GET.get('page')) - 25 + 1
                context['countpage'] = page
        return context


class HomeViews1(TemplateView):
    template_name = 'musics/home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['music_trakss'] = MusicTrack.objects.all()
        return context