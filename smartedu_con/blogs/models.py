from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class Category(models.Model):
    name    =   models.CharField(max_length=100,null=True)
    slug    =   models.SlugField(max_length=110,null=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name    =   models.CharField(max_length=100,null=True)
    slug    =   models.SlugField(max_length=110,null=True)

    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    image       =   models.ImageField(upload_to="blogs/%Y/%m/%d/",default="courses/default_course_image.jpg")
    header      =   models.CharField(max_length=400)
    description =   models.TextField(max_length=100)
    text        =   RichTextField()
    category    =   models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    tags        =   models.ManyToManyField(Tag,blank=True,null=True)
    date        =   models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.header

    

class BlogComments(models.Model):
    author      =   models.CharField(max_length=400)
    date        =   models.DateField(auto_now=True)
    text        =   models.TextField(max_length=1000)
    username    =   models.CharField(max_length=400)
    email       =   models.CharField(max_length=1000)
    blog        =   models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.author
    
    
