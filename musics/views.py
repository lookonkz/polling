from django.shortcuts import render, redirect
import json
from django.views import View
from django.contrib.contenttypes.models import ContentType
from .models import LikeDislike, Music
from django.http import HttpResponse
from django.views.generic.list import ListView
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from g_recaptcha.validate_recaptcha import validate_captcha
from .models import Music



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

        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
            }),
            content_type="application/json"
        )


class MusicList(ListView):
    model = Music
    context_object_name = 'music_list'
    template_name = 'musics/music_list.html'
    paginate_by = 50

#
# @validate_captcha
# def register(request):
#     GOOGLE_RECAPTCHA_SITE_KEY = settings.GOOGLE_RECAPTCHA_SITE_KEY
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create(username=form.cleaned_data['username'], password='dafadsfa$rRRR',
#                                        email=form.cleaned_data['email'])
#             user.save()
#             auth.login(request, user)
#             return redirect('musics/')
#     else:
#         form = LoginForm()
#     return render(request, 'musics/register.html', {'form': form, 'context': GOOGLE_RECAPTCHA_SITE_KEY})
#


@validate_captcha
def register(request):
    GOOGLE_RECAPTCHA_SITE_KEY = settings.GOOGLE_RECAPTCHA_SITE_KEY
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['username'], password='dafadsfa$rRRR',
                                       email=form.cleaned_data['email'])
            user.save()
            auth.login(request, user)
            return redirect('musics/')
    else:
        form = UserRegistrationForm()
    return render(request, 'musics/register.html', {'form': form, 'context': GOOGLE_RECAPTCHA_SITE_KEY})
