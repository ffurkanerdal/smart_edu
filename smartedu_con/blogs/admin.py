from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class Category(admin.ModelAdmin):
    prepopulated_fields =   {"slug":("name",)}
    
@admin.register(Tag)
class Tag(admin.ModelAdmin):
    prepopulated_fields =   {"slug":("name",)}

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display    =   ("header","image")
    search_fields   =   ["header","text"]

@admin.register(BlogComments)
class BlogComments(admin.ModelAdmin):
    list_display    =   ("author","date")
    search_fields   =   ["author"]


