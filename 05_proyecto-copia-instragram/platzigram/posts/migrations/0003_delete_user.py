# Generated by Django 3.1.7 on 2021-03-30 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
