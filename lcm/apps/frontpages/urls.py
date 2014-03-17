from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lcm.apps.frontpages.views.home', name='home'),
    url(r'^about/$', 'lcm.apps.frontpages.views.about', name='about'),
    url(r'^stories/$', 'lcm.apps.frontpages.views.stories', name='stories'),
    url(r'^stories/(\d+)/$', 'lcm.apps.frontpages.views.story', name='story'),
    url(r'^partners/$', 'lcm.apps.frontpages.views.partners', name='partners'),
    url(r'^partner/(\d+)/$', 'lcm.apps.frontpages.views.partner', name='partner'),
    url(r'^ministry/$', 'lcm.apps.frontpages.views.ministry', name='ministry'),
    url(r'^contact/$', 'lcm.apps.frontpages.views.contact', name='contact')
)
