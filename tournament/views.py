from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.views.generic.edit import FormView

from tournament.forms import TournamentRegistrationForm

# Create your views here.
class PlayerView(FormView):
    template_name = "page/player_registration.html"
    form_class = TournamentRegistrationForm
    success_url = "/player/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        enquiry = form.save(commit=False)
        messages.success(self.request, "Your message has been sent successfully")

        body = get_template("emails/contact-email.html").render({"enquiry": enquiry})

        msg = EmailMessage(
            "MBC - Contact Form completed",
            body,
            settings.FROM_EMAIL,
            [settings.TO_EMAIL],
        )
        msg.content_subtype = "html"

        msg.send()
        enquiry.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)