# Generated by Django 3.2 on 2021-04-20 16:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0011_anuncio_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='updated',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Última actualización'),
        ),
    ]
