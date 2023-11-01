from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Scorecard
from .forms import ScorecardForm


@login_required
def scorecard_index(request):
    scorecards = Scorecard.objects.all()
    return render(
        request, "scorecards/scorecard-index.html", {"scorecards": scorecards}
    )


@login_required
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
    
@login_required
def view_scorecard(request, scorecard_id):
    scorecard = get_object_or_404(Scorecard, id=scorecard_id)

    context = {
        "scorecard": scorecard,
    }

    return render(request, "scorecards/view-scorecard.html", context)
