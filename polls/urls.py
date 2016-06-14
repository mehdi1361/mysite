from django.conf.urls import url
from . import views


urlpatterns =[
      url(r'^question/(?P<question_id>\d+)/detail/$', views.detail, name='detail'),
      url(r'^$', views.index, name='index'),
    ]
