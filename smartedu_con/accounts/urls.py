from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import (
    UserLoginView,UserRegisterView,
    UserLogout,UserDashboard,
    EnrollTheCourse,ReleaseTheCourse
    )

urlpatterns =   [
    path("login/",UserLoginView.as_view(),
         name='login'),
    path("register/",UserRegisterView.as_view(),
         name='register'),
    path("dashboard/",UserDashboard.as_view(), 
         name='dashboard'),
    path("enroll_the_course/",EnrollTheCourse.as_view(), 
         name='enroll_the_course'),
    path("release_the_course/",ReleaseTheCourse.as_view(), 
         name='release_the_course'),
    path("logout/",UserLogout.as_view(), 
         name='logout'),
     path('password_change/', auth_views.PasswordChangeView.as_view(),
          name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), 
         name='password_change_done'),
]