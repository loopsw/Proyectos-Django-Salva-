# Generated by Django 3.2 on 2021-04-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0019_alter_anuncio_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Última actualización'),
        ),
    ]
