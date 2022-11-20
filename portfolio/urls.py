
from django.urls import include, re_path
import portfolio.views as views

urlpatterns = [
    re_path(r'^$', views.home, name='main'),
    re_path(r'^about$', views.about, name='about'),
    re_path(r'^arch$', views.arch, name='arch'),
    re_path(r'^masters-thesis$', views.mastersThesis, name='masters-thesis'),
    re_path(r'^thesis$', views.thesis, name='thesis'),
    re_path(r'^research$', views.research, name='research'),
    re_path(r'^cv$', views.cv, name='cv'),
    re_path(r'^code$', views.code, name='code'),
    re_path(r'^proj/(?P<id>[0-9]+)$', views.proj, name='project'),
    re_path(r'^get-all-images/', views.getAllImages, name='get-all-images'),
    re_path(r'^get-all-projects/', views.getAllProjects, name='get-all-projects'),
    re_path(r'^get-projects-by-year/(?P<year>[0-5])', views.getProjectByYear, name='get-projects-by-year'),
    re_path(r'^get-thesis-by-topic/(?P<topic>[-\w]+)', views.getThesisTopic, name='get-thesis-by-topic'),
    re_path(r'^get-thesis-topics/', views.getThesisTopics, name='get-thesis-topics'),
    re_path(r'^get-masters-images/', views.getMastersImages, name='get-masters-images'),
]
