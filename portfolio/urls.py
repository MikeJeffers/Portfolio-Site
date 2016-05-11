
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.home, name='main'),
    url(r'^get-image/', views.getImage, name='get-image'),
    url(r'^get-all-images/', views.getAllImages, name='get-all-images'),
]
