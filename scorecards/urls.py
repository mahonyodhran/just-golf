from django.urls import path
from .views import add_scorecard, scorecard_index, view_scorecard

urlpatterns = [
    path("", scorecard_index, name="scorecard-index"),
    path("add-course", add_scorecard, name="add-scorecard"),
    path("<int:scorecard_id>/", view_scorecard, name="view-scorecard"),
]