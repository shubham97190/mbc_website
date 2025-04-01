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
from tournament.models import Tournament


class PlayerView(FormView):
    template_name = "page/player_registration.html"
    form_class = TournamentRegistrationForm
    success_url = "/registration/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tournament_data"] = Tournament.objects.filter(status=0, is_current_active=True).first()
        context["thumbnails"] = HomePageCarousel.objects.filter(is_visible=True).order_by("updated_date")[9:15]
        return context

    def form_valid(self, form):
        print(form)
        registration = form.save(commit=False)
        registration.created_by_id = 1
        registration.updated_by_id = 1
        messages.success(self.request, "Your registration has been submitted successfully")

        body = get_template("emails/contact-email.html").render({"enquiry": registration})

        msg = EmailMessage(
            "MMB - Registration Form completed",
            body,
            settings.FROM_EMAIL,
            [settings.TO_EMAIL],
        )
        msg.content_subtype = "html"

        # msg.send()
        registration.save()
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
