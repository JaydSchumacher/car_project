from django.conf.urls import url
from . import views

def test(request):
    print 701

urlpatterns = [
    url(r'^add$', views.addcar),
    url(r'^create$', views.create),
    url(r'^$', views.dashboard),
    

]