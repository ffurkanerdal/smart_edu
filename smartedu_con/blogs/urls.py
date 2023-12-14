from django.urls import path
from blogs.views import *


urlpatterns =   [
    path("",BlogList.as_view(),name="blogs"),
    path("<slug:category_slug>/<int:blog_id>",BlogDetail.as_view(),name="blog_detail"),
    path("categories/<slug:category_slug>",BlogList.as_view(),name="blogs_by_category"),
    path("tags/<slug:tag_slug>",BlogList.as_view(),name="blogs_by_tags"),
    path("search/",Search.as_view(),name="search")
]