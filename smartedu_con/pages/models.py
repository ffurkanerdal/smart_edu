from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name  =   models.CharField(max_length=100)
    last_name   =   models.CharField(max_length=100)
    email       =   models.EmailField()
    phone       =   models.CharField(max_length=100)
    message     =   models.TextField(blank=True)

    def __str__(self) -> str:
        return self.email