from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from .manager import LikeDislikeManager
from django.utils import timezone
from django.utils.functional import cached_property
from easy_thumbnails.fields import ThumbnailerImageField
from django.core.validators import FileExtensionValidator
from django.urls import reverse
import os


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


class Category(models.Model):
    name = models.CharField(verbose_name='название категории', default=None,  max_length=100, blank=True)
    slug = models.SlugField(verbose_name='название ссылки категории', default=None, max_length=100, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создание', default=timezone.now, blank=True)
    updated_at = models.DateTimeField(verbose_name='дата обнолвения', default=timezone.now, blank=True)
    icon = models.CharField(verbose_name='иконка', max_length=13, null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)

    @cached_property
    def music_trakss(self):
        return self.musictrack_set.all()


# Клипы
class MusicClip(models.Model):
    name = models.CharField(verbose_name='Название песни', max_length=100)
    music = models.CharField(verbose_name='ссылка', max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    votes = GenericRelation(LikeDislike, related_query_name='musics/photo', default=None, blank=True)
    article_date = models.DateTimeField('Дата публикации', auto_now_add=timezone.now, blank=True)
    reiting = models.IntegerField(verbose_name='количество голосов', default=0, blank=True)
    sorted_list = models.SmallIntegerField(verbose_name='порядок', db_index=True, default=1, blank=True)

    class Meta:
        verbose_name = 'Клип'
        verbose_name_plural = 'Клипы'
        ordering = ['sorted_list']

    def __str__(self):
        return self.name


# def get_music_path(instance, filename):
#     return os.path.join('music/tracks/', "{}".format(instance.name), filename)


# Музыка
class MusicTrack(models.Model):
    name = models.CharField(verbose_name='Название песни', max_length=100)
    music = models.FileField(verbose_name='музыка', upload_to='music/tracks/', validators=[FileExtensionValidator(
        allowed_extensions=['mp3', 'wav'])])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    votes = GenericRelation(LikeDislike, related_query_name='musics/track', default=None, blank=True)
    article_date = models.DateTimeField('Дата публикации', auto_now_add=timezone.now, blank=True)
    reiting = models.IntegerField(verbose_name='количество голосов', default=0, blank=True)
    sorted_list = models.SmallIntegerField(verbose_name='порядок', db_index=True, default=1, blank=True)
    image = ThumbnailerImageField(verbose_name='фото', upload_to='musics/track/img', null=True,
                                  default='musics/track/img/logo1.png', blank=True)

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Треки'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('musics:track', kwargs={'pk':self.pk})


class GolosMus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(MusicTrack, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'music']
        verbose_name = 'Голоса'
        verbose_name_plural = 'Голоса'

    def __str__(self):
        return '{}'.format(self.id)