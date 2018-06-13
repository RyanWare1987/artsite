from django.conf.urls import url
from .views import view_basket, add_to_basket, adjust_basket

urlpatterns = [
    url(r'^$', view_basket, name='view_basket'),
    url(r'^add/(?P<id>\d+)', add_to_basket, name='add_to_basket'),
    url(r'^adjust/(?P<id>\d+)', adjust_basket, name='adjust_basket'),
    ]