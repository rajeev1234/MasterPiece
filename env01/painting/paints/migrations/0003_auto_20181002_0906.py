# Generated by Django 2.1.1 on 2018-10-02 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paints', '0002_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='post',
            name='read_time',
        ),
    ]
