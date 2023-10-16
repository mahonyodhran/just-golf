from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", views.course_index, name="course-index"),
    path("add-course", views.add_course, name="add-course"),
]