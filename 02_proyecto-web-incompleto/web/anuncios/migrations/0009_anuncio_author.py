# Generated by Django 3.2 on 2021-04-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0008_remove_anuncio_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='author',
            field=models.CharField(default='undefined', max_length=150, verbose_name='Autor de la publicacion'),
        ),
    ]
