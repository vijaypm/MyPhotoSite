__author__ = 'vijay'
from django.conf.urls import patterns, url, include

from MyPhotos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^add/$', views.add_album, name='add_album'),
    url(r'^(?P<album_id>\d+)/photos/$', views.photos, name='photos'),

)