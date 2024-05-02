from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import render
from accounts import views as av

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'index.html'), name='home'),
    path("register/", av.register_view, name="register"),
    path("login/", av.login_view, name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
