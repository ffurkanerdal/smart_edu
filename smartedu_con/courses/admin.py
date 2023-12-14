from django.contrib import admin
from . models import Course,Category,Tag,CourseComments
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display    =   ("name","available")
    list_filter     =   ("available",)
    search_fields   =   ["name","description"]

@admin.register(CourseComments)
class CourseComment(admin.ModelAdmin):
    list_display    =   ("author","rate")
    search_fields   =   ["author","rate"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields =   {"slug":("name",)}
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields =   {"slug":("name",)}