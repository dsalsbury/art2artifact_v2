from django.conf.urls import patterns, url

from coins import views

urlpatterns = patterns('',
     # ex: /coins/
     url(r'^$', views.index, name='index'),
                       
     # ex: /coins/5/
     url(r'^(?P<coin_id>\d+)/$', views.coin, name='detail'),

     # ex: /corpus/5/
     url(r'^corpus/(?P<corpus_id>\d+)/$', views.corpus, name='corpus'),

     # ex: /view_collection/
     url(r'^view_collection.html', views.view_collection, name='view_collection'),

     # ex: /view_corpora/
     url(r'^view_corpora.html', views.view_corpora, name='view_corpora'),                 
)
