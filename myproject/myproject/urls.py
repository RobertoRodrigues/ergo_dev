from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'core.views.homepage'),
    # (r'^evaluation/', include('ergocoin.urls', namespace='ergocoin')),
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
)

# Configuracao para o Grappelli
urlpatterns += patterns('', (r'^grappelli/', include('grappelli.urls')),)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': "/home/rrodrigues/webapps/ergo_dev/myproject/static/"}),
) #Configuracao para servir arquivos estaticos pelo django
