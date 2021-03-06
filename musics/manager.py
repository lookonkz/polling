from django.db import models
from django.db.models import Sum


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    # def musics(self):
    #     return self.get_queryset().filter(content_type__model='music').order_by('-musics__pub_date')

    def musictrack(self):
        return self.get_queryset().filter(content_type__model='musictrack').order_by('-musics__pub_date')
