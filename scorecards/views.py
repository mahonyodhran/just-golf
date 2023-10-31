from django.shortcuts import render
from django.http import HttpResponse
from .models import Scorecard
from .forms import ScorecardForm

def scorecard_index(request):
    scorecards = Scorecard.objects.all()
    return render(request, "scorecards/scorecard-index.html", {"scorecards": scorecards})

def add_scorecard(request):
    if request.method == "POST":
        form = ScorecardForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home.html")
        else:
            return HttpResponse("<p>Info is not Valid</p>")

    else:
        form = ScorecardForm
        context = {
            "form": form,
        }

        return render(request, "scorecards/add-scorecard.html", context)