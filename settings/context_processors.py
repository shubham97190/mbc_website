import random
from .models import *
from tournament.models import Tournament

def settings(request):
    active_tournament = Tournament.objects.filter(is_current_active=True).first()
    active_tournament_year = active_tournament.tournament_date_time.year if active_tournament else None
    return {
        'settings': WebsiteSettings.get_solo(),
        'client': sorted(Client.objects.all(), key=lambda x: random.random())[:6],
        'active_tournament': active_tournament,
        'active_tournament_year': active_tournament_year,
    }
