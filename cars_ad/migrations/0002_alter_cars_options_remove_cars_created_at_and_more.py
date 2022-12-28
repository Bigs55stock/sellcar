# Generated by Django 4.1.4 on 2022-12-28 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_ad', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['make']},
        ),
        migrations.RemoveField(
            model_name='cars',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='cars',
            name='desc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cars',
            name='img',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='cars',
            name='make',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cars',
            name='model',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cars',
            name='price',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cars',
            name='year',
            field=models.CharField(max_length=150),
        ),
    ]