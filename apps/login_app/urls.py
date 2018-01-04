from django.conf.urls import url
from . import views

def test(request):
    print 701

urlpatterns = [
    url(r'^$', views.index),
    url(r'^userprofile/(?P<id>\d+)$', views.userprofile),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout', views.logout),
]