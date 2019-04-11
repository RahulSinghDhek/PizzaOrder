from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from pizzaorder.test_MM.views import PersonViewset,CaseViewSet
    url(r'^person/$', PersonViewset.as_view(), name='album-list'),
    url(r'^case/$', CaseViewSet.as_view(), name='track-list'),
    #url(r'^orders/(?P<pk>[0-9]+)/$', OrderDataViewSet.as_view(), name='order-detail'),
]