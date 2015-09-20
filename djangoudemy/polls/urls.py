from django.conf.urls import url
from polls import views

'''
The urlspatterns variable is a list of url functions.
They take as arguments:
1. An url
2. A view, defined in views.py
3. A global view name, for namespacing

We use an empty string (^$) because the last config file removed the 'polls' part, used to get here.
'''

urlpatterns = [url(r'^$' , views.index, name='index'),
               url(r'^(?P<questionID>[0-9]+)/$' , views.detail , name='detail'),
               url(r'^(?P<questionID>[0-9]+)/results$' , views.results , name='results'),
               url(r'^(?P<questionID>[0-9]+)/vote$' , views.vote , name='vote'),]
