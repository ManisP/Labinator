from django.conf.urls import patterns, url
from polls import views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^test$', views.TestView.as_view(), name='test'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^test/(?P<pk>[0-9]+)/$', views.LabView.as_view(), name='lab'),
    url(r'^test/(?P<lab_id>[0-9]+)/submit/$', views.submit, name='submit'),
    url(r'^test/(?P<pk>[0-9]+)/labresults/$', views.LabResultsView.as_view(), name='labresults'),
]
