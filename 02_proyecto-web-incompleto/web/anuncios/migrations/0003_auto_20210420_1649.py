# Generated by Django 3.2 on 2021-04-20 14:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0002_auto_20210420_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='author',
            field=models.TextField(default=django.utils.timezone.now, max_length=150, verbose_name='Autor de la publicacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anuncio',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Última actualización'),
            preserve_default=False,
        ),
    ]
