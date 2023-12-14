from django.urls import path
from .views import CourseList,CourseDetail,Search

urlpatterns    =   [
    path('',CourseList.as_view(), name="courses"),
    path('<slug:category_slug>/<int:course_id>',CourseDetail.as_view(),name="course_detail"),
    path('categories/<slug:category_slug>',CourseList.as_view(),name="courses_by_category"),
    path('tags/<slug:tag_slug>',CourseList.as_view(),name="courses_by_tag"),
    path('courses/search/',Search.as_view(), name="course_search")
]
