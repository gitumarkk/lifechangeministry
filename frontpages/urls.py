from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'frontpages.views.home', name='home'),
    url(r'^about/$', 'frontpages.views.about', name='about'),
    url(r'^stories/$', 'frontpages.views.stories', name='stories'),
    url(r'^partners/$', 'frontpages.views.partners', name='partners'),
    url(r'^donations/$', 'frontpages.views.donations', name='donations'),
    url(r'^contact/$', 'frontpages.views.contact', name='contact')
)
