from django.urls import path
from . import views
from .views import DeleteView

urlpatterns = [
    path("", views.course_index, name="course-index"),
    path("add-course", views.add_course, name="add-course"),
    path('delete-course/<int:pk>/', DeleteView.as_view(), name='delete-course'),
]