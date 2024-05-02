from django.shortcuts import redirect
from django.urls import reverse

class RedirectIfLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (request.path == reverse('login') or request.path == reverse('register')) and request.user.is_authenticated:
            return redirect('home')
        response = self.get_response(request)
        return response