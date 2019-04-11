from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from orders.views import PizzaViewSet,CustomerViewSet,OrderDataViewSet

urlpatterns = [
    url(r'^customers/$', CustomerViewSet.as_view(), name='customer-list'),
    url(r'^pizzaorders/$', OrderDataViewSet.as_view(), name='order-list'),
    url(r'^pizza/$', PizzaViewSet.as_view(), name='pizza-list'),
    #url(r'^orders/(?P<pk>[0-9]+)/$', OrderDataViewSet.as_view(), name='order-detail'),
]