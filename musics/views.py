from django.views import View
from django.contrib.contenttypes.models import ContentType
from .models import LikeDislike, MusicTrack
from django.views.generic import TemplateView, ListView, DetailView
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
            else:
                likedislike.delete()
                obj.reiting = obj.reiting - 1
                obj.save()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            obj.reiting = obj.reiting + 1
            obj.save()
            result = True

        return JsonResponse({
                "result": result,
                "like_count": obj.reiting,
                "dislike_count": obj.votes.dislikes().count(),
            })


class HomeViews(ListView):
    template_name = 'musics/home.html'
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


class TrackDetailView(DetailView):
    model = MusicTrack
    template_name = 'musics/trackdetai.html'
    context_object_name = 'track'
