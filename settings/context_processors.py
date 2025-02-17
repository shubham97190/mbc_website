import random
from .models import *

def settings(request):
    return {
        'settings': WebsiteSettings.get_solo(),
        'client': sorted(Client.objects.all(), key=lambda x: random.random())[:6],
    }
