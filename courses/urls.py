from django.urls import path
from .views import DeleteView, add_course, add_tee, course_index, view_course

urlpatterns = [
    path("", course_index, name="course-index"),
    path("add-course", add_course, name="add-course"),
    path('delete-course/<int:pk>/', DeleteView.as_view(), name='delete-course'),
    path("<int:course_id>/", view_course, name="view-course"),
    path("add-tee", add_tee, name="add-tee"),
]