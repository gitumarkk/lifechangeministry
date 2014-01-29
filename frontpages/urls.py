from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'frontpages.views.home', name='home'),
    url(r'^about/$', 'frontpages.views.about', name='about'),
    url(r'^contact/$', 'frontpages.views.contact', name='contact')
)
