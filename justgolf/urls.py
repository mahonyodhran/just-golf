from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("about", TemplateView.as_view(template_name="about.html"), name="about"),
    path("courses/", include("courses.urls")),
    path("scorecards/", include("scorecards.urls")),
]
