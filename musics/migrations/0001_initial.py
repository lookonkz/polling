# Generated by Django 2.0.6 on 2018-06-28 11:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, verbose_name='название категории')),
                ('slug', models.SlugField(blank=True, default=None, max_length=100, verbose_name='название ссылки категории')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='дата создание')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='дата обнолвения')),
                ('icon', models.CharField(blank=True, default=None, max_length=13, null=True, verbose_name='иконка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(-1, 'Не нравится'), (1, 'Нравится')], verbose_name='Голос')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='дата создание')),
                ('updated_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='дата обнолвения')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'лайк',
                'verbose_name_plural': 'лайки',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='MusicClip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название песни')),
                ('music', models.CharField(max_length=300, verbose_name='ссылка')),
                ('article_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('reiting', models.IntegerField(blank=True, default=0, verbose_name='количество голосов')),
                ('sorted_list', models.SmallIntegerField(blank=True, db_index=True, default=1, verbose_name='порядок')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musics.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Клип',
                'verbose_name_plural': 'Клипы',
                'ordering': ['sorted_list'],
            },
        ),
        migrations.CreateModel(
            name='MusicTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название песни')),
                ('music', models.FileField(upload_to='music/tracks/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])], verbose_name='музыка')),
                ('article_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('reiting', models.IntegerField(blank=True, default=0, verbose_name='количество голосов')),
                ('sorted_list', models.SmallIntegerField(blank=True, db_index=True, default=1, verbose_name='порядок')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musics.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Музыка',
                'verbose_name_plural': 'Треки',
                'ordering': ['sorted_list'],
            },
        ),
    ]
