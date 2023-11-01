from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import CourseForm, TeeForm
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    context_object_name = "course"
    success_url = reverse_lazy("course-index")

@login_required
def course_index(request):
    courses = Course.objects.all()
    return render(request, "courses/course-index.html", {"courses": courses})

@login_required
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

@login_required
def view_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    tees = course.tee_set.all()

    context = {
        'course': course,
        'tees': tees,
    }

    return render(request, 'courses/view-course.html', context)

@login_required
def add_tee(request):
    if request.method == "POST":
        form = TeeForm(request.POST)
        if form.is_valid():
            tee = form.save(commit=False)
            if tee.is_colour_available():
                tee.save()
                return render(request, "home.html")
            else:
                return HttpResponse("<p>The selected color already exists for this course.</p>")
        else:
            return HttpResponse("<p>Info is not valid.</p>")

    else:
        form = TeeForm
        context = {
            "form": form,
        }

        return render(request, "courses/add-tee.html", context)