# Generated by Django 2.0.3 on 2018-03-29 08:21

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='music/photo', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='music',
            name='music',
            field=models.CharField(max_length=300, verbose_name='ссылка'),
        ),
    ]
