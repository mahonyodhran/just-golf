from django.forms import ModelForm
from .models import Course, Tee

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ["name", "eircode"]
        
class TeeForm(ModelForm):
    class Meta:
        model = Tee
        fields = ["course", "colour", "slope", "par", "yards"]