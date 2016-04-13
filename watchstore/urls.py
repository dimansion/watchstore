from django.conf.urls import patterns, url
from watchstore import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^men/$', views.men, name='men'),
    url(r'^men/(?P<pk>[0-9]+)/$', views.watch_detail, name='watch_detail'),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

