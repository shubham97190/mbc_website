from django.urls import path
from tournament.views import PlayerView, TournamentTncView, TournamentListView, TournamentDetailsView

urlpatterns = [
    path('registration/', PlayerView.as_view(), name='registration'),
    path('tournament-list/', TournamentListView.as_view(), name='tournament-list'),
    path('tournament-details/<int:pk>/', TournamentDetailsView.as_view(), name='tournament-details'),
    path('tournament-tnc/<int:pk>/', TournamentTncView.as_view(), name='tournament-tnc')
]