# Generated by Django 3.1 on 2023-12-12 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rate',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=1000, null=True, upload_to='')),
                ('author', models.CharField(max_length=400)),
                ('text', models.TextField(max_length=1000)),
                ('rate', models.FloatField(null=True)),
                ('date', models.DateField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
