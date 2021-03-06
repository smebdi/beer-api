# Generated by Django 2.0.4 on 2018-09-19 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerapp', '0002_dislike_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='dislike',
            name='address',
            field=models.CharField(default='cmd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dislike',
            name='image_url',
            field=models.CharField(default='cmd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dislike',
            name='type',
            field=models.CharField(default='cmd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='address',
            field=models.CharField(default='cmd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='image_url',
            field=models.CharField(default='cmd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='type',
            field=models.CharField(default='cmd', max_length=255),
            preserve_default=False,
        ),
    ]
