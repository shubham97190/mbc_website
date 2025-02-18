from django.contrib.sitemaps.views import sitemap
from django.urls import path
from page.views import *
from page.sitemaps import PageViewSitemap
from page.sitemaps import GenericViewSitemap

sitemaps = {
    'page': PageViewSitemap,
    'generic': GenericViewSitemap,
}

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailPageView.as_view(), name='blog-detail'),
    # path('roaster/', EnterprisePageView.as_view(), name='roaster'),
    # path('roaster/<slug:slug>/', EnterpriseSubPageView.as_view(), name='roaster-sub-page'),
    path('membership/', MembershipPageView.as_view(), name='membership'),
    path('location/', LocationPageView.as_view(), name='location'),
    path('rules/', RulesPageView.as_view(), name='rules'),
    path('sitemap/', SitemapPageView.as_view(), name='sitemap'),
    path('<slug:slug>/', GenericPageView.as_view(), name='page'),

]

if settings.DEBUG:
    urlpatterns += [
        path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    ]
