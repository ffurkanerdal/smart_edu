# Generated by Django 3.1 on 2023-12-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageDesign', '0006_abouttextcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouttextcontent',
            name='iamge',
            field=models.ImageField(default=1, max_length=1000, upload_to=''),
            preserve_default=False,
        ),
    ]
