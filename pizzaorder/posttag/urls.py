from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posttag.views import TagViewSet,PostViewSet

urlpatterns = [
    url(r'^tag/$', TagViewSet.as_view(), name='tag-list'),
    url(r'^post/$', PostViewSet.as_view(), name='post-list'),
    #url(r'^pizza/$', PizzaViewSet.as_view(), name='pizza-list'),
    #url(r'^orders/(?P<pk>[0-9]+)/$', OrderDataViewSet.as_view(), name='order-detail'),
]