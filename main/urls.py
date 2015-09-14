from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', 'main.views.thejqs', name='thejqs'),
    url(r'^about/$', 'main.views.about', name='about'),
    url(r'^portfolio/$', 'main.views.portfolio', name='portfolio'),
]
