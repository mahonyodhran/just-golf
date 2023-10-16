from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .forms import CourseForm
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    context_object_name = "course"
    success_url = reverse_lazy("course-index")


def course_index(request):
    courses = Course.objects.all()
    return render(request, "courses/course-index.html", {"courses": courses})


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
        else:
            return HttpResponse("<p>Info is not Valid</p>")

    else:
        form = CourseForm
        context = {
            "form": form,
        }

        return render(request, "courses/add-course.html", context)