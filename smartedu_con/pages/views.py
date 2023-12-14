from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from courses.views import Course
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from smartedu.views import BaseView
from pageDesign.models import *
from blogs.models import *


# Create your views here.

class IndexView(BaseView):
    template_name   =   'index.html'
    def get_context_data(self, **kwargs):
        context                 =   super().get_context_data(**kwargs)
        context['courses']      =   Course.objects.filter(available=True).order_by('-data')[:2]
        context['total_course'] =   Course.objects.filter(available=True).count()
        context['sliders']      =   Slider.objects.all()
        context['about']        =   SiteDetails.objects.filter(name='About').first()
        context['history']      =   History.objects.all()
        context['testimonials'] =   Comments.objects.all()
        context['testiText']    =   SiteDetails.objects.filter(name='Testimonials')
        context['testiBanner']  =   Banners.objects.filter(name='testimonials').first()
        context['referencess']  =   References.objects.all()
        context['main_content'] =   Banners.objects.filter(name="MainContent").first()
        context['blogs']        =   Blog.objects.all()

        return context

class AboutView(BaseView):
    template_name   =   'about.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        mvs     =   MissionVisionHistory.objects.filter
        about   =   AboutContent.objects.filter(id=1).first()
        context =   super().get_context_data(**kwargs)

        context['mission'], context['vision'], context['history']   =   mvs(name='Mission').first(), mvs(name='Vision').first(), mvs(name='History').first()
        context['pageName'], context['pageText'], context['banner']  =   about.header, about.text, about.image.url
        context['contents']     =   AboutTextContent.objects.all()
        context['referencess']  =   References.objects.all()
        context['testimonials'] =   Comments.objects.all()
        context['testiBanner']  =   Banners.objects.filter(name='testimonials').first()
        context['referencess']  =   References.objects.all()
        context["banner"]       =   Banners.objects.filter(name="About Us").first()
        
        return context

class ContactView(SuccessMessageMixin,FormView,BaseView):
    template_name   =   "contact.html"
    form_class      =   ContactForm
    success_url     =   reverse_lazy('contact')
    success_message =   "We received your message"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["banner"] =   Banners.objects.filter(name="Contact").first()
        return context

    def form_valid(self, form: Any) -> HttpResponse:
        form.save()
        return super().form_valid(form)
    
