from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .forms import CourseForm
from .models import Course


def course_index(request):
    courses = Course.objects.all()
    return render(request, "courses/course-index.html", {"courses": courses})


def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<p>Course Saved!</p>")
        else:
            return HttpResponse("<p>Info is not Valid</p>")

    else:
        form = CourseForm
        context = {
            "form": form,
        }

        return render(request, "courses/add-course.html", context)
