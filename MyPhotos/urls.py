__author__ = 'vijay'
from django.conf.urls import patterns, url

from MyPhotos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>\d+)/profile/$', views.profile, name='profile'),
    url(r'^(?P<user_id>\d+)/albums/$', views.albums, name='albums'),
    url(r'^(?P<album_id>\d+)/photos/$', views.photos, name='photos'),
)