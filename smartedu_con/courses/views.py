from typing import Any
from django import http
from django.shortcuts import render, get_object_or_404
from smartedu.views import BaseView
from . models import Course,Category,Tag
from pageDesign.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CourseList(BaseView):
    template_name = 'courses.html'
    items_per_page  =   2
    def get(self, request, category_slug=None, tag_slug=None, 
            *args: Any, **kwargs: Any):
        category_page = None
        tag_page = None
        current_user = request.user

        if category_slug is not None:
            category_page = get_object_or_404(Category, slug=category_slug)
            courses = Course.objects.filter(available=True, 
                                            category=category_page)
        elif tag_slug is not None:
            tag_page = get_object_or_404(Tag, slug=tag_slug)
            courses = Course.objects.filter(available=True, tags=tag_page)
        else:
            if current_user.is_authenticated:
                enrolled_courses = current_user.joined_courses.all()
                courses = Course.objects.all().order_by('-data')
                for course in enrolled_courses:
                    courses = courses.exclude(id=course.id)
            else:
                courses = Course.objects.all().order_by('-data')

        paginator   =   Paginator(courses,self.items_per_page)
        page        =   request.GET.get("page")

        try:
            courses =   paginator.page(page)
        except PageNotAnInteger:
            courses     =   paginator.page(1)
        except EmptyPage:
            courses     =   paginator.page(paginator.num_pages)


        return render(request, self.template_name, 
                      self.get_context_data(courses=courses))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context["banner"]     =   Banners.objects.filter(name="Courses").first()

        return context

class CourseDetail(BaseView):
    template_name   =   'course.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =   super().get_context_data(**kwargs)
        cate                =   Category.objects.filter(slug=self.category_slug).first()
        context['course']   =   Course.objects.get(id=int(self.course_id))
        context['courses']      =   self.courses
        context['categories']   =   Category.objects.all()
        context['tags']         =   Tag.objects.all()
        context["cate_courses"] =   Course.objects.filter(category=cate.id).all()
        return context
    
    def get(self, request, category_slug, course_id, *args: Any, **kwargs: Any):
        self.category_slug  =   category_slug
        self.course_id      =   course_id
        self.courses        =   Course.objects.all()

        current_user        =   request.user

        if current_user.is_authenticated:
            self.enrolled_courses   =   current_user.joined_courses.all()
        else:
            self.enrolled_courses   =   self.courses

        return render(request,self.template_name,self.get_context_data())

class Search(BaseView):
    template_name = 'courses.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        request = self.request  # request'i almak için bu satırı ekleyin.
        context['courses'] = Course.objects.filter(name__contains=request.GET.get('search', ''))
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['banner']   =   Banners.objects.filter(name="Courses").first()
        return context
