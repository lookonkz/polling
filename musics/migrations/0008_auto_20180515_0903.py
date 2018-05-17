# Generated by Django 2.0.3 on 2018-05-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0007_auto_20180402_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['sorted_list'], 'verbose_name': 'Музыка', 'verbose_name_plural': 'Музыка'},
        ),
        migrations.AddField(
            model_name='music',
            name='sorted_list',
            field=models.SmallIntegerField(blank=True, db_index=True, default=1, verbose_name='порядок'),
        ),
    ]
