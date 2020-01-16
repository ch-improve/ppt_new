from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.Index.as_view()),
    url(r'^demo/$', views.Demo.as_view())
]