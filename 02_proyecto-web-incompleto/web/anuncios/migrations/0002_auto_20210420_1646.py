# Generated by Django 3.2 on 2021-04-20 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncio',
            name='author',
        ),
        migrations.RemoveField(
            model_name='anuncio',
            name='updated',
        ),
    ]
