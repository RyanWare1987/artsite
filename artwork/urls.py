from django.conf.urls import url, include
from django.contrib import admin
from artsite import views
from .views import productsall, productdetail, checkout
from django.conf import settings 


urlpatterns = [
    url(r'^home/$', views.index, name='home'),
    url(r'^products/(?P<id>\d+)/$', productdetail),
    url(r'^products/$', productsall, name='products'),
    url(r'^$', checkout, name='checkout'),



    url(r'^pages/', include('django.contrib.flatpages.urls')),
]