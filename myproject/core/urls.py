from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('myproject.core.views',
    url(r'^$', 'homepage', name='homepage'),
)

