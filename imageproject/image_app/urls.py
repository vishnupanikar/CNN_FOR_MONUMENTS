from django.conf.urls import include, url
from image_app import views
from django.urls import path

from . import views

# after the url from urls(imageproject) the flow is directed to this url specifiedd in this file
# Which in turn calls the calls ImageCreateAPIView to insert data
urlpatterns = [
    url(r'^upload/$', views.ImageCreateAPIView.as_view()),

]