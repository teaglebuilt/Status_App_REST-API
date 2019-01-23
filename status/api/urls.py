from django.conf.urls import url
from .views import (
    StatusAPIView,
    StatusDetailAPIView
)

app_name = 'api-status'

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusDetailAPIView.as_view(), name='detail')
]
