from django.urls import path
from tournament.views import PlayerView

urlpatterns = [
    path('player/', PlayerView.as_view(), name='player')
]