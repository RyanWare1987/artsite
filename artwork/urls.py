from django.conf.urls import url, include
from django.contrib import admin
from artsite import views
from .views import productsall, productdetail
from django.conf import settings 


urlpatterns = [
    url(r'^home/$', views.index, name='home'),
    #url(r'^register/$', register, name='register'),
    #url(r'^profile/$', profile, name='profile'),
    #url(r'^image_form_upload/$', image_form_upload, name='image_form_upload'),
    url(r'^products/(?P<id>\d+)/$', productdetail),
    url(r'^products/$', productsall, name='products'),
    #url(r'^productdetail/$', productdetail, name='productdetail'),



    url(r'^pages/', include('django.contrib.flatpages.urls')),
]