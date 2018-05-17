from django.conf.urls import url, include
from django.contrib import admin
from artsite import views
from .views import login, logout, register, profile, image_form_upload
from django.conf import settings 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.index, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^image_form_upload/$', image_form_upload, name='image_form_upload'),


    url(r'^pages/', include('django.contrib.flatpages.urls')),
]
