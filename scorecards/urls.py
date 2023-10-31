from django.urls import path
from .views import scorecard_index

urlpatterns = [
    path("", scorecard_index, name="scorecard-index"),
]