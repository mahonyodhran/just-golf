from django.shortcuts import render
from .models import Scorecard

def scorecard_index(request):
    scorecards = Scorecard.objects.all()
    return render(request, "scorecards/scorecard-index.html", {"scorecards": scorecards})