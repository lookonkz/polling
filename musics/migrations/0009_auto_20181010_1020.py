# Generated by Django 2.0.3 on 2018-10-10 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0008_auto_20181010_0438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musictrack',
            options={'ordering': ['name'], 'verbose_name': 'Музыка', 'verbose_name_plural': 'Треки'},
        ),
    ]
