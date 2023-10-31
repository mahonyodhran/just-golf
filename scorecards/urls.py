from django.urls import path
from .views import add_scorecard, scorecard_index

urlpatterns = [
    path("", scorecard_index, name="scorecard-index"),
    path("add-course", add_scorecard, name="add-scorecard"),
]