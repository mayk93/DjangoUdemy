from django.conf.urls import url
from polls import views

#Please see 'pollsUrlsDetails.txt' in the root directory for more details.

urlpatterns = [url(r'^$' , views.IndexView.as_view() , name='index'),
               url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name='detail'),
               url(r'^(?P<pk>[0-9]+)/results$' , views.ResultsView.as_view() , name='results'),
               url(r'^(?P<questionID>[0-9]+)/vote$' , views.vote , name='vote'),]
