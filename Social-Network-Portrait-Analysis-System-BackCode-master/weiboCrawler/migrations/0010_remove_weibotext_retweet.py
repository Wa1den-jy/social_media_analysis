# Generated by Django 2.2.19 on 2021-04-13 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weiboCrawler', '0009_auto_20210413_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weibotext',
            name='retweet',
        ),
    ]
