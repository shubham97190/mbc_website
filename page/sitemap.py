from django.contrib import sitemaps
from django.core.urlresolvers import reverse

from page.models import GenericPage


class PageViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['page:home', 'page:for_business', 'page:for_you', 'page:membership', 'page:about', 'page:blog',
                'page:faqs', 'page:contact', 'page:developers', ]

    def location(self, item):
        return reverse(item)


class GenericViewSitemap(sitemaps.Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return GenericPage.objects.all()
