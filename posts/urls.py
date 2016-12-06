from django.conf.urls import url
from .views import (
    ListView,
    DetailView
)

urlpatterns = [
    url(r'^$', ListView.as_view(), name='list'),
    url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(), name='detail'),
]
