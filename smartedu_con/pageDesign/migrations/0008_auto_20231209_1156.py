# Generated by Django 3.1 on 2023-12-09 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pageDesign', '0007_abouttextcontent_iamge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abouttextcontent',
            old_name='iamge',
            new_name='image',
        ),
    ]
