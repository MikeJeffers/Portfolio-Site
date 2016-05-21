
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.home, name='main'),
    url(r'^arch$', views.arch, name='arch'),
    url(r'^thesis$', views.thesis, name='thesis'),
    url(r'^research$', views.research, name='research'),
    url(r'^cv$', views.cv, name='cv'),
    url(r'^code$', views.code, name='code'),
    url(r'^proj/(?P<id>[0-9]+)$', views.proj, name='project'),
    url(r'^get-image/', views.getImage, name='get-image'),
    url(r'^get-all-images/', views.getAllImages, name='get-all-images'),
    url(r'^get-all-projects/', views.getAllProjects, name='get-all-projects'),
]
