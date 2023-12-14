from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from teachers.models import Teacher
from courses.models import Course
from courses.views import BaseView
from pageDesign.models import *

class TeacherListView(BaseView):
    model   =   Teacher
    template_name   =   "teachers.html"
    context_object_name =   "teachers"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        context["teachers"] =   Teacher.objects.all()
        context["banner"]   =   Banners.objects.filter(name="Teachers").first()
        context["comments"] =   Comments.objects.all()
        context["testiBan"] =   Banners.objects.filter(name="testimonials").first()
        context["references"]   =   References.objects.all()
        return context

class TeacherDetailView(BaseView):
    model = Teacher
    template_name = "teacher.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        teacher_instance = Teacher.objects.get(pk=self.kwargs["pk"])
        
        context["teacher"] = teacher_instance
        context["courses"] = Course.objects.filter(available=True, teacher=teacher_instance)
        
        return context