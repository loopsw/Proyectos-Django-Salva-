# Generated by Django 3.2.4 on 2021-06-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_alter_empresa_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='content',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Título'),
        ),
    ]
