# Generated by Django 3.1 on 2023-11-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20231124_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(max_length=110, null=True, unique=True)),
            ],
        ),
    ]
