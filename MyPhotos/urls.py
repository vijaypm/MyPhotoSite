__author__ = 'vijay'
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static

from MyPhotos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^add/$', views.add_album, name='add_album'),
    url(r'^(?P<album_id>\d+)/photos/$', views.photos, name='photos'),
    url(r'^(?P<album_id>\d+)/photos/add/$', views.add_photo, name='add_photo'),
    url(r'^(?P<album_id>\d+)/photos/(?P<photo_id>\d+)/del/$', views.del_photo, name='del_photo'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)