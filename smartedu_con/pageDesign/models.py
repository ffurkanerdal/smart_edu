from django.db import models

# Create your models here.
class PageNavbar(models.Model):
    name    = models.CharField(max_length=100)
    url     = models.SlugField(max_length=110)

    def __str__(self) -> str:
        return self.name

class Slider(models.Model):
    image   = models.ImageField(max_length=1000)
    name    = models.CharField(max_length=200)
    url     = models.CharField(max_length=200,null=True)
    text    = models.CharField(max_length=1000,null=True)

    def __str__(self) -> str:
        return self.name

class History(models.Model):
    image   =   models.ImageField(max_length=1000)
    year    =   models.CharField(max_length=50)
    text    =   models.TextField(max_length=700)

    def __str__(self) -> str:
        return self.year

class Comments(models.Model):
    author  =   models.CharField(max_length=200)
    header  =   models.CharField(max_length=200)
    text    =   models.TextField(max_length=200)
    image   =   models.ImageField(max_length=1000)

    def __str__(self) -> str:
        return self.header

class Footer(models.Model):
    header  =   models.CharField(max_length=200)
    url     =   models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.header

class AboutContent(models.Model):
    image   = models.ImageField(max_length=1000,null=True)
    header  = models.CharField(max_length=500)
    text    = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return self.header


class MissionVisionHistory(models.Model):
    name    =   models.CharField(max_length=200)
    header  =   models.CharField(max_length=200)
    text    =   models.TextField(max_length=400)

    def __str__(self) -> str:
        return self.name

class Logo(models.Model):
    image   = models.ImageField(max_length=1000)

class References(models.Model):
    name    =   models.CharField(max_length=500)
    image   =   models.ImageField(max_length=1000)

    def __str__(self) -> str:
        return self.name

class SiteDetails(models.Model):
    name    =   models.CharField(max_length=100)
    data    =   models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name

class SocialMedia(models.Model):
    name    =   models.CharField(max_length=100)
    url     =   models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name

class Banners(models.Model):
    image   =   models.ImageField(max_length=1000)
    name    =   models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.name
    
class AboutTextContent(models.Model):
    subHeader   =   models.CharField(max_length=1000)
    header      =   models.CharField(max_length=1000)
    text        =   models.TextField(max_length=500)
    image       =   models.ImageField(max_length=1000)

    def __str__(self) -> str:
        return self.header
