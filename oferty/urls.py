from django.conf.urls import include, url
from . import views

urlpatterns = [
    # /oferty/
    url(r'^$', views.index, name='index'),

    # /ofery/ID/
    url(r'^(?P<items_id>[0-9]+)$', views.detail, name='detail'),
]
