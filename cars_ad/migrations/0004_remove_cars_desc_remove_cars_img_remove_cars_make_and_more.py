# Generated by Django 4.1.4 on 2023-01-03 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_ad', '0003_alter_cars_options_cars_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='img',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='make',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='model',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='year',
        ),
    ]
