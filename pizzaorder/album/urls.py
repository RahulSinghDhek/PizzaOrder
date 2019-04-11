from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from album.views import AlbumViewSet,TrackViewSet
urlpatterns = [
    url(r'^albums/$', AlbumViewSet.as_view(), name='album-list'),
    url(r'^tracks/$', TrackViewSet.as_view(), name='track-list'),
    #url(r'^orders/(?P<pk>[0-9]+)/$', OrderDataViewSet.as_view(), name='order-detail'),
]