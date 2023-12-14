from django.contrib import admin
from .models import *



# Register your models here.

@admin.register(PageNavbar)
class Navbar(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'url')
    
    class Meta:
        app_label = 'Navbar'

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'text')
    search_fields = ('name','image', 'text')

@admin.register(History)
class History(admin.ModelAdmin):
    class Meta:
        app_label = 'History'

@admin.register(Comments)
class Comment(admin.ModelAdmin):
    class Meta:
        app_label = 'Comments'

@admin.register(Footer)
class Footer(admin.ModelAdmin):
    class Meta:
        app_label = 'Footer'
 
@admin.register(AboutContent)
class AboutContent(admin.ModelAdmin):
    class Meta:
        app_label   =   ('About Content')

@admin.register(MissionVisionHistory)
class MissonVisionAbout(admin.ModelAdmin):
    class Meta:
        app_label   =   ('Mission Vision About')

@admin.register(Logo)
class Logo(admin.ModelAdmin):
    class Meta:
        app_label   =   ('Logo')

@admin.register(References)
class References(admin.ModelAdmin):
    list_display    =   ('name','image')
    search_fields   =   ('name','image')

    class Meta:
        app_label   =   ('References')

@admin.register(SiteDetails)
class SiteDetails(admin.ModelAdmin):
    list_display    =   ('name','data')
    search_fields   =   ('name','data')

    class Meta:
        app_label   =   ('Site Deails')

@admin.register(SocialMedia)
class SocialMedia(admin.ModelAdmin):
    list_display    =   ('name','url')
    search_fields   =   ('name','url')

    class Meta:
        app_label   =   ('Social Media')

@admin.register(Banners)
class Banners(admin.ModelAdmin):
    list_display    =   ('name','image')
    search_fields   =   ('name','image')

    class Meta:
        app_label   =   ('Banners')

@admin.register(AboutTextContent)
class AboutTextContent(admin.ModelAdmin):
    list_display    =   ("header","subHeader")
    searcH_fields   =   ("header","subheader")

    class Meta:
        app_label   =   ("About Text Content")