from django.conf.urls import url

from .views import index, detail, results, vote

app_name = 'polls'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^([0-9]+)/$', detail, name='detail'),
    url(r'^([0-9]+)/results/$', results, name='results'),
    url(r'^([0-9]+)/vote/$', vote, name='vote'),
]
