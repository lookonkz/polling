# Generated by Django 2.0.6 on 2019-11-18 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musics', '0009_auto_20181010_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='GolosMus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musics.MusicTrack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Голоса',
                'verbose_name_plural': 'Голоса',
            },
        ),
        migrations.AlterUniqueTogether(
            name='golosmus',
            unique_together={('user', 'music')},
        ),
    ]