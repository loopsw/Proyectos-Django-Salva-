# Generated by Django 3.2 on 2021-04-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0003_auto_20210420_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='author',
            field=models.TextField(max_length=150, null=True, verbose_name='Autor de la publicacion'),
        ),
    ]
