# Generated by Django 4.2.8 on 2023-12-12 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog_description_blog_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
    ]
