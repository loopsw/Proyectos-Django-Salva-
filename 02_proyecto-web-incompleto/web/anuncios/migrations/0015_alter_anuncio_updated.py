# Generated by Django 3.2 on 2021-04-21 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0014_alter_anuncio_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Última actualización'),
        ),
    ]
