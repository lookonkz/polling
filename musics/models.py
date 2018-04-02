from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from .manager import LikeDislikeManager
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='дата создание', default=timezone.now, blank=True)
    updated_at = models.DateTimeField(verbose_name='дата обнолвения', default=timezone.now, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey()
    objects = LikeDislikeManager()

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'
        ordering = ['user']

    def __str__(self):
        return '{}'.format(self.user)


# Create your models here.
class Music(models.Model):
    name = models.CharField(verbose_name='Название песни', max_length=100)
    music = models.CharField(verbose_name='ссылка', max_length=300)
    votes = GenericRelation(LikeDislike, related_query_name='musics/photo', default=None, blank=True)
    article_date = models.DateTimeField('Дата публикации', auto_now_add=timezone.now, blank=True)
    reiting = models.IntegerField(verbose_name='количество голосов', default=0, blank=True)

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'
        ordering = ['-reiting']

    def __str__(self):
        return self.name




