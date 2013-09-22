from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyPhotoSite.views.home', name='home'),
    # url(r'^MyPhotoSite/', include('MyPhotoSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myphotos/', include('MyPhotos.urls', namespace="myphotos")),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^accounts/profile/$',TemplateView.as_view(template_name="myphotos/index.html")), # not needed because LOGIN_REDIRECT_URL in settings.py
)
