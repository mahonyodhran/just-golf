from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Golfer

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    gender = forms.ChoiceField(choices=Golfer.GENDER_CHOICES, required=False)
    index = forms.FloatField(required=False)

    class Meta:
        model = Golfer
        fields = ["username", "email", "password1", "password2", "gender", "index"]