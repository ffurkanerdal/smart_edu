from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name    =   models.CharField(max_length=100,null=True)
    slug    =   models.SlugField(max_length=110,null=True,unique=True)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name    =   models.CharField(max_length=100,null=True)
    slug    =   models.SlugField(max_length=110,null=True,unique=True)

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    teacher     =   models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    name        =   models.CharField(max_length=200, unique=True)
    category    =   models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    tags        =   models.ManyToManyField(Tag,blank=True,null=True)
    description =   models.TextField(blank=True,null=True)
    students    =   models.ManyToManyField(User,blank=True,related_name="joined_courses")
    image       =   models.ImageField(upload_to="courses/%Y/%m/%d/",default="courses/default_course_image.jpg")
    data        =   models.DateTimeField(auto_now=True)
    available   =   models.BooleanField(default=True)
    rate        =   models.FloatField(default=0)

    def __str__(self) -> str:
        return self.name
    
class CourseComments(models.Model):
    image   =   models.ImageField(max_length=1000,null=True)
    author  =   models.CharField(max_length=400)
    text    =   models.TextField(max_length=1000)
    rate    =   models.FloatField(null=True)
    date    =   models.DateField(auto_now=True)
    course  =   models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.author

