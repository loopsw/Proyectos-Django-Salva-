# Generated by Django 3.2 on 2021-04-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('texto', models.TextField(verbose_name='Contenido')),
                ('author', models.TextField(max_length=150, verbose_name='Autor de la publicacion')),
                ('image', models.ImageField(null=True, upload_to='images', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Última actualización')),
                ('estado', models.CharField(choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='borrador', max_length=10)),
            ],
        ),
    ]
