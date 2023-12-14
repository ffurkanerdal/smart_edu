from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from courses.models import Course
from typing import Any
from smartedu.views import BaseView
from pageDesign.models import *

class UserLoginView(BaseView):
    template_name   =   'login.html'
    def post(self,request,*args,**kwargs):
        form    =   LoginForm(request.POST)

        if form.is_valid():
            username    =   form.cleaned_data['username']
            password    =   form.cleaned_data['password']
            user        =   authenticate(request,username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    messages.success(request,'Login Succesful!')
                    return redirect('index')
                else:
                    messages.error(request,'Disabled Account')
            else:
                messages.error(request,'Check Your Username Or Password')
                form = LoginForm()
        else:
            messages.error(request,'Invalid form submission. Please check the form.')
            form = LoginForm()
        
        return render(request,self.template_name,{'form': form})
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =   super().get_context_data(**kwargs)
        context['form'] =   LoginForm()
        print(context["view"])
        return context

class UserRegisterView(BaseView):
    template_name   =   'register.html'
    def post(self,request,*args,**kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Account has been created you can login')
            return redirect('login')
        else:
            messages.error(request,'Account has not been created you can try again register')
            form    =   RegisterForm()
        
        return render(request,self.template_name,{'form':form})
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =   super().get_context_data(**kwargs)
        context['form'] =   RegisterForm()
        
        return context

class UserLogout(BaseView):
    template_name   =   'index.html'
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("index")

class EnrollTheCourse(BaseView):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated: return redirect('login')
        course_id = int(request.POST.get('course_id'))
        user_id = int(request.POST.get('user_id'))
        course = Course.objects.get(id=course_id)
        user = User.objects.get(id=user_id)
        course.students.add(user)
        return redirect('dashboard')

class ReleaseTheCourse(BaseView):
    def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated: return redirect('login')
        course_id = int(request.POST.get('course_id'))
        user_id = int(request.POST.get('user_id'))
        course      =   Course.objects.get(id=course_id)
        user        =   User.objects.get(id=user_id)
        course.students.remove(user)
        return redirect('dashboard')

@method_decorator(login_required, name='dispatch')
class UserDashboard(BaseView):
    template_name = 'dashboard.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        courses = current_user.joined_courses.all()
        context['courses'] = courses
        context['current_user'] =   self.request.user
        
        return context
