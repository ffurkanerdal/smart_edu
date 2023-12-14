from django.urls import path,include
from pages.views import AboutView,IndexView,ContactView


urlpatterns =   [
    path('',IndexView.as_view(), name="index"),
    path('home',IndexView.as_view(), name="index"),
    path('about',AboutView.as_view(),name="about"),
    path('contact',ContactView.as_view(),name="contact"),
]
