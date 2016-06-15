from django.conf.urls import url
# from . import views
from .views import IndexView, DetailView, ResultView,vote


urlpatterns =[
      url(r'^question/(?P<pk>\d+)/detail/$', DetailView.as_view(), name='detail'),
      url(r'^question/(?P<pk>\d+)/result/$', ResultView.as_view(), name='result'),
      url(r'^$', IndexView.as_view(), name='index'),
      url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
    ]


# urlpatterns =[
#       url(r'^question/(?P<question_id>\d+)/detail/$', views.detail, name='detail'),
#       url(r'^question/(?P<question_id>\d+)/result/$', views.result, name='result'),
#       url(r'^$', views.index, name='index'),
#       url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
#     ]
