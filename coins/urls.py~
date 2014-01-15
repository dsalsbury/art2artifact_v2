from django.conf.urls import patterns, url

from coins import views

urlpatterns = patterns('',
     # ex: /coins/
     url(r'^$', views.index, name='index'),
                       
     # ex: /coins/5/
     url(r'^(?P<coin_id>\d+)/$', views.coin, name='detail'),

     # ex: /view_collection/
     url(r'^view_collection.html', views.view_collection, name='view_collection'),
)
