from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ergocoin.views',
    url(r'^$', 'question', name = 'question')),
)
