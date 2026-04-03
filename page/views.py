from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.db.models import Prefetch
from django.template.loader import get_template
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from blog.models import Article
from enquiry.forms import EnquiryForm
from faq.models import Question
from fixtures.models import Fixtures
from tournament.models import Tournament, TournamentCategory, TournamentWinnerPage
from .models import *
from location.models import Location
from rules.models import Rules


# Create your views here.


class HomePageView(TemplateView):
    template_name = "page/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Home.objects.all()
        context["tournament"] = Tournament.objects.filter(show_on_home=True) \
            .prefetch_related(Prefetch('tournamentcategory_set',
                                       queryset=TournamentCategory.objects.filter(is_active=True).order_by('code'),
                                       to_attr='categories'
                                       )).order_by("tournament_date_time").first()
        context["cimages"] = HomePageCarousel.objects.filter(is_visible=True).order_by("updated_date")[:8]
        return context


class AboutPageView(TemplateView):
    template_name = "page/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = About.get_solo()
        return context


class ContactPageView(FormView):
    template_name = "page/contact.html"
    form_class = EnquiryForm
    success_url = "/contact/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Contact.get_solo()
        return context

    def form_valid(self, form):
        enquiry = form.save(commit=False)
        # form.send_email()
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


class MembershipPageView(TemplateView):
    template_name = "page/membership.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Membership.objects.all()
        return context


class FAQPageView(TemplateView):
    template_name = "page/faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = FAQ.get_solo()
        context["questions"] = Question.objects.all()
        return context


class BlogPageView(ListView):
    paginate_by = 9
    model = Article
    template_name = "page/blog.html"
    context_object_name = "blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Blog.get_solo()
        return context

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        qs = qs.filter(published=True)
        return qs


class BlogDetailPageView(DetailView):
    model = Article
    context_object_name = "blog_post"
    template_name = "page/blog-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Blog.get_solo()
        return context


class GenericPageView(DetailView):
    model = GenericPage
    context_object_name = "page"
    template_name = "page/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SitemapPageView(TemplateView):
    template_name = "page/sitemap.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Article.objects.filter(published=True).order_by("-date")
        context["genericpage"] = GenericPage.objects.all()
        return context


class LocationPageView(TemplateView):
    template_name = "page/location.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = Location.objects.all()
        return context


class RulesPageView(TemplateView):
    template_name = "page/rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rules"] = Rules.objects.all()
        return context


class FixturesPageView(TemplateView):
    template_name = "page/fixtures.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fixtures"] = Fixtures.objects.all()
        context["tournament"] = Tournament.objects.filter(show_on_home=True) \
            .prefetch_related(Prefetch('tournamentcategory_set',
                                       queryset=TournamentCategory.objects.filter(is_active=True).order_by('code'),
                                       to_attr='categories'
                                       )).order_by("tournament_date_time").first()
        return context


class WinnersListView(ListView):
    template_name = "page/winners.html"
    context_object_name = "winner_pages"

    def get_queryset(self):
        return TournamentWinnerPage.objects.filter(is_published=True).select_related("tournament").order_by("-tournament__tournament_date_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active = Tournament.objects.filter(is_current_active=True).first()
        current_winner = None
        past_winners = context["winner_pages"]
        if active:
            current_winner = past_winners.filter(tournament=active).first()
            past_winners = past_winners.exclude(tournament=active)
        context["current_winner"] = current_winner
        context["past_winners"] = past_winners
        return context


class WinnerDetailView(DetailView):
    model = TournamentWinnerPage
    template_name = "page/winner-detail.html"
    context_object_name = "winner"

    def get_queryset(self):
        return TournamentWinnerPage.objects.filter(is_published=True).select_related("tournament")
