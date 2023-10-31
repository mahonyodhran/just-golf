from django import forms
from .models import Scorecard

class ScorecardForm(forms.ModelForm):
    class Meta:
        model = Scorecard
        fields = '__all__'