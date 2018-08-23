# Generated by Django 2.0.3 on 2018-05-24 04:49

from django.db import migrations, models
import django.db.models.deletion
import musics.models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0010_auto_20180524_0424'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название песни')),
                ('music', models.FileField(upload_to=musics.models.get_music_path, verbose_name='музыка')),
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
        migrations.AlterModelOptions(
            name='musicclip',
            options={'ordering': ['sorted_list'], 'verbose_name': 'Клип', 'verbose_name_plural': 'Клипы'},
        ),
    ]