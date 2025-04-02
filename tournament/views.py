from django.utils.timezone import now
from django.views.generic import ListView

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from page.models import HomePageCarousel
from tournament.forms import TournamentRegistrationForm

# Create your views here.
from tournament.models import Tournament, Player


def send_email(registration):
    body = get_template("emails/player_form_submit.html").render({"player": registration})
    msg = EmailMessage(
        "Milton Masters Badminton - Registration Form completed",
        body,
        settings.FROM_EMAIL,
        [registration.email],
    )
    msg.content_subtype = "html"
    msg.send()


class PlayerView(FormView):
    template_name = "page/player_registration.html"
    form_class = TournamentRegistrationForm
    success_url = "/registration/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t: Tournament = Tournament.objects.filter(status=0, is_current_active=True).first()
        p = Player.objects.filter(tournament=t, is_active=True).count()
        context["tournament_data"] = t
        context["thumbnails"] = HomePageCarousel.objects.filter(is_visible=True).order_by("updated_date")[9:15]
        context["is_registration_open"] = t and t.last_registration_date > now() and t.total_allowed_registration >= p
        return context

    def form_valid(self, form):
        print(form)
        registration = form.save(commit=False)
        registration.created_by_id = 1
        registration.updated_by_id = 1

        registration.save()
        registration.category.set(self.request.POST.getlist('category'))
        send_email(registration)
        messages.success(self.request, "Your registration has been submitted successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class TournamentDetailsView(DetailView):
    model = Tournament
    template_name = 'page/tournament-details.html'


class TournamentTncView(DetailView):
    model = Tournament
    template_name = 'page/tnc-modal.html'


class TournamentListView(ListView):
    paginate_by = 10
    model = Tournament
    template_name = "page/tournament-list.html"
    context_object_name = "tournaments"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        qs = qs.filter(is_current_active=True).order_by('-tournament_date_time')
        return qs
