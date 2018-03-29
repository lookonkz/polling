# Generated by Django 2.0.3 on 2018-03-29 11:52

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0002_auto_20180329_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='article_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='music',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, default=None, upload_to='music/photo', verbose_name='Фото'),
        ),
    ]
