
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.home, name='main'),
    url(r'^about$', views.about, name='about'),
    url(r'^arch$', views.arch, name='arch'),
    url(r'^thesis$', views.thesis, name='thesis'),
    url(r'^research$', views.research, name='research'),
    url(r'^cv$', views.cv, name='cv'),
    url(r'^code$', views.code, name='code'),
    url(r'^proj/(?P<id>[0-9]+)$', views.proj, name='project'),
    url(r'^get-all-images/', views.getAllImages, name='get-all-images'),
    url(r'^get-all-projects/', views.getAllProjects, name='get-all-projects'),
    url(r'^get-projects-by-year/(?P<year>[0-5])', views.getProjectByYear, name='get-projects-by-year'),
    url(r'^get-thesis-by-topic/(?P<topic>\w+)', views.getThesisTopic, name='get-thesis-by-topic'),
    url(r'^get-thesis-topics/', views.getThesisTopics, name='get-thesis-topics'),
]
