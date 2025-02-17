from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from blog.models import Article
from enquiry.forms import EnquiryForm
from faq.models import Question
from .models import *


# Create your views here.


class HomePageView(TemplateView):
    template_name = "page/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Home.get_solo()
        context["blogs"] = Article.objects.all().order_by("-date")[:3]
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
        context["membership"] = Membership.objects.all()
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
