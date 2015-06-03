from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from zinnia.urls import urlpatterns as _urlpatterns

admin.autodiscover()

blog_urls = [
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^tags/', include('zinnia.urls.tags')),
    url(r'^feeds/', include('zinnia.urls.feeds')),
    url(r'^random/', include('zinnia.urls.random')),
    url(r'^authors/', include('zinnia.urls.authors')),
    url(r'^categories/', include('zinnia.urls.categories')),
    url(r'^comments/', include('zinnia.urls.comments')),
    url(r'^entries/', include('zinnia.urls.entries')),
    # url(r'^archives/', include('zinnia.urls.archives')),
    url(r'^', include('zinnia.urls.archives')),
    url(r'^shortlink/', include('zinnia.urls.shortlink')),
    url(r'^quickentry/', include('zinnia.urls.quick_entry'))
]


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'lcm.views.home', name='home'),
    url(r'^', include('lcm.apps.frontpages.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include(blog_urls)),
    url(r'^captcha/', include('captcha.urls')),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}


urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),)
